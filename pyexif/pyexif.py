# -*- coding: utf-8 -*-
from PIL import Image, ExifTags


def _convert_to_degrees(value):
    """
    Helper function to convert the GPS coordinates stored
    in the EXIF to degress in float format
    """
    hours = float(value[0][0]) / float(value[0][1])
    minutes = float(value[1][0]) / float(value[1][1])
    seconds = float(value[2][0]) / float(value[2][1])
    return hours + (minutes / 60.0) + (seconds / 3600.0)


class Exif:

    def __init__(self, image, **kwargs):
        """
        sample code:
        from pyexif import pyexif
        r = pyexif.Exif('YOUR_IMAGE')
        print (r.lat)  # extract the latitude
        """

        self.image = self._load_image(image)
        self._get_exif_data()

    def _load_image(self, image_file_name):
        """Load the image from the given source"""

        try:
            return Image.open(image_file_name)
        except IOError:
            raise IOError('No such file')

    def _get_exif_data(self):
        """Get embedded EXIF data from image file. """

        self.exif_raw_data = None
        try:
            if hasattr(self.image, '_getexif'):
                self.exif_raw_data = self.image._getexif().items()
        except AttributeError:
            raise AttributeError('Image does not contain exif data')

    def parse(self, exif_tag):
        """Parse exif tags"""
        for tag, value in self.exif_raw_data:
            if ExifTags.TAGS.get(tag, None) == exif_tag:
                return value
            elif type(value) is dict:
                for k, v in value.items():
                    if exif_tag == ExifTags.GPSTAGS.get(k, None):
                        return v

    @property
    def exif_version(self):
        return self.parse('ExifVersion')

    @property
    def gps_attributes(self):
        attr = []
        for k, v in self.parse('GPSInfo').items():
            attr.append(ExifTags.GPSTAGS.get(k, None))
        return attr

    @property
    def lat(self):
        if self.lat_ref == 'S':
            return -_convert_to_degrees(self.parse('GPSLatitude'))
        return _convert_to_degrees(self.parse('GPSLatitude'))

    @property
    def lon(self):
        if self.lon_ref == 'W':
            return -_convert_to_degrees(self.parse('GPSLongitude'))
        return _convert_to_degrees(self.parse('GPSLongitude'))

    @property
    def lat_ref(self):
        return self.parse('GPSLatitudeRef')

    @property
    def lon_ref(self):
        return self.parse('GPSLongitudeRef')

    @property
    def altitude_ref(self):
        ref_code = self.parse('GPSAltitudeRef')
        if ref_code == '0':
            return 'Sea level'
        elif ref_code == '1':
            return 'Sea level reference (negative value)'
        else:
            return None

    @property
    def altitude(self):
        alt = self.parse('GPSAltitude')
        if alt:
            return float(alt[0]) / float(alt[1])
        return None
