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
            [BASE_DIR, 'glacier_national_park.jpg']
        )
        self.fname_with_exif_southern_hemisphere = '/'.join(
            [BASE_DIR, 'new_zealand_wellington_beehive.jpg']
        )
        self.fname_ioerror = '/'.join(
            [BASE_DIR, '']
        )
        return self

    def test_image_without_exif_data(self):
        data = pyexif.get_exif_data(self.fname_no_exif)
        result = pyexif.get_lat_lon(data)
        self.assertEqual(result, False)

    def test_no_image(self):
        data = pyexif.get_exif_data(self.fname_ioerror)
        self.assertEqual(data, ''.join(['IOERROR ', self.fname_ioerror]))
        result = pyexif.get_lat_lon(data)
        self.assertEqual(result, False)

    def test_image_with_exif_data_northern_hemisphere(self):
        data = pyexif.get_exif_data(self.fname_with_exif_northern_hemisphere)
        result = pyexif.get_lat_lon(data)
        self.assertAlmostEqual(result[0], 48.7390111111)
        self.assertAlmostEqual(result[1], -113.749747222)

    def test_image_with_exif_data_southern_hemisphere(self):
        data = pyexif.get_exif_data(self.fname_with_exif_southern_hemisphere)
        result = pyexif.get_lat_lon(data)
        self.assertAlmostEqual(result[0], -41.277833333333)
        self.assertAlmostEqual(result[1], 174.777166666666)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
