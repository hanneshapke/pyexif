# -*- coding: utf-8 -*-
from PIL import Image, ExifTags


def get_exif_data(fname):
    """
    Get embedded EXIF data from image file.
    """
    exif_gps_data = {}
    try:
        img = Image.open(fname)
        if hasattr(img, '_getexif'):
            exifinfo = img._getexif()
            if exifinfo is not None:
                for tag, value in exifinfo.items():
                    decoded = ExifTags.TAGS.get(tag, tag)
                    if decoded == "GPSInfo":
                        gps_data = {}
                        for data in value:
                            decoded = ExifTags.GPSTAGS.get(data, data)
                            gps_data[decoded] = value[data]
                        exif_gps_data[decoded] = gps_data
                    else:
                        exif_gps_data[decoded] = value
    except IOError:
        return 'IOERROR ' + fname
    return exif_gps_data


def get_exif_gps(exif_data):
    if 'GPSImgDirection' in exif_data:
        return exif_data['GPSImgDirection']
    else:
        False


def convert_to_degrees(value):
    """
    Helper function to convert the GPS coordinates stored
    in the EXIF to degress in float format
    """
    hours = float(value[0][0]) / float(value[0][1])
    minutes = float(value[1][0]) / float(value[1][1])
    seconds = float(value[2][0]) / float(value[2][1])
    return hours + (minutes / 60.0) + (seconds / 3600.0)


def get_lat_lon(exif_data):
    """
    Returns the latitude and longitude, if available,
    from the provided exif_data (obtained through get_exif_data above)
    """
    lat = None
    lon = None

    gps_info = get_exif_gps(exif_data)
    if not gps_info:
        return False

    gps_latitude = gps_info.get('GPSLatitude', None)
    gps_latitude_ref = gps_info.get('GPSLatitudeRef', None)
    gps_longitude = gps_info.get('GPSLongitude', None)
    gps_longitude_ref = gps_info.get('GPSLongitudeRef', None)

    if gps_latitude and gps_latitude_ref \
            and gps_longitude and gps_longitude_ref:
        lat = convert_to_degrees(gps_latitude)
        if gps_latitude_ref != "N":
            lat = 0 - lat
        lon = convert_to_degrees(gps_longitude)
        if gps_longitude_ref != "E":
            lon = 0 - lon

    return lat, lon

# # How to test the code
# def _test(fname):
#     data = get_exif_data(fname)
#     result = get_lat_lon(data)
#     print result
