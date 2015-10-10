# -*- coding: utf-8 -*-
from PIL import Image, ExifTags


class Exif:

    def __init__(self, **kwargs):
        """
        sample code:
        from pyexif.pyexif import Exif
        r = Exif.load_image('YOUR_IMAGE')
        print (r.lat)  # extract the latitude
        """
        pass

    @staticmethod
    def convert_to_degrees(value):
        """
        Helper function to convert the GPS coordinates stored
        in the EXIF to degress in float format
        """
        hours = float(value[0][0]) / float(value[0][1])
        minutes = float(value[1][0]) / float(value[1][1])
        seconds = float(value[2][0]) / float(value[2][1])
        return hours + (minutes / 60.0) + (seconds / 3600.0)

    @staticmethod
    def get_exif_data(image):
        """Get embedded EXIF data from image file. """
        try:
            if hasattr(image, '_getexif'):
                return image._getexif().items()
        except AttributeError:
            raise AttributeError('Image does not contain exif data')

    @classmethod
    def load_image(cls, image_file_name):
        """Load the image from the given source"""

        try:
            exif_obj = cls()
            exif_obj.image = Image.open(image_file_name)
            exif_obj.exif_raw_data = exif_obj.get_exif_data(exif_obj.image)
            return exif_obj
        except IOError:
            raise IOError('No such file')

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
            return -self.convert_to_degrees(self.parse('GPSLatitude'))
        return self.convert_to_degrees(self.parse('GPSLatitude'))

    @property
    def lon(self):
        if self.lon_ref == 'W':
            return -self.convert_to_degrees(self.parse('GPSLongitude'))
        return self.convert_to_degrees(self.parse('GPSLongitude'))

    @property
    def lat_ref(self):
        return self.parse('GPSLatitudeRef')

    @property
    def lon_ref(self):
        return self.parse('GPSLongitudeRef')

    @property
    def altitude_ref(self):
        ref_code = self.parse('GPSAltitudeRef')
        if ref_code == b'0':
            return 'Sea level'
        elif ref_code == b'1':
            return 'Sea level reference (negative value)'
        else:
            return None

    @property
    def altitude(self):
        alt = self.parse('GPSAltitude')
        if alt:
            return float(alt[0]) / float(alt[1])
        return None
