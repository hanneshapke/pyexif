#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyexif
----------------------------------

Tests for `pyexif` module.
"""

import os
import unittest

from pyexif import pyexif


class TestPyexif(unittest.TestCase):

    def setUp(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.fname_no_exif = '/'.join(
            [BASE_DIR, 'no_exif_data.jpg']
        )
        self.fname_with_exif_northern_hemisphere = '/'.join(
            [BASE_DIR, 'mt_south_sister_or.jpg']
        )
        self.fname_with_exif_southern_hemisphere = '/'.join(
            [BASE_DIR, 'new_zealand_wellington_beehive.jpg']
        )
        self.fname_ioerror = '/'.join(
            [BASE_DIR, '']
        )
        return self

    def test_image_without_exif_data(self):
        with self.assertRaises(AttributeError) as context:
            pyexif.Exif(self.fname_no_exif)
        self.assertEqual(
            'Image does not contain exif data',
            str(context.exception))

    def test_no_image(self):
        with self.assertRaises(IOError) as context:
            pyexif.Exif(self.fname_ioerror)
        self.assertEqual(
            'No such file',
            str(context.exception))

    def test_image_with_exif_data_northern_hemisphere(self):
        gps_attr = [
            'GPSLatitudeRef',
            'GPSLatitude',
            'GPSLongitudeRef',
            'GPSLongitude',
            'GPSAltitudeRef',
            'GPSAltitude',
            'GPSTimeStamp',
            'GPSSpeedRef',
            'GPSSpeed',
            'GPSImgDirectionRef',
            'GPSImgDirection',
            'GPSDestBearingRef',
            'GPSDestBearing',
            'GPSDateStamp'
        ]

        result = pyexif.Exif(self.fname_with_exif_northern_hemisphere)
        self.assertAlmostEqual(result.lat, 44.10364444444445, delta=0.0001)
        self.assertAlmostEqual(result.lon, -121.76937222222222, delta=0.0001)
        self.assertEqual(str(result.exif_version), '0221')
        self.assertEqual(result.gps_attributes, gps_attr)
        self.assertEqual(result.altitude_ref, None)
        self.assertAlmostEqual(result.altitude, 3150.3488372, delta=0.0001)

    def test_image_with_exif_data_southern_hemisphere(self):
        result = pyexif.Exif(self.fname_with_exif_southern_hemisphere)
        self.assertAlmostEqual(result.lat, -41.277833333333, delta=0.0001)
        self.assertAlmostEqual(result.lon, 174.777166666666, delta=0.0001)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
