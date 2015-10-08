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
        with self.assertRaises(AttributeError) as context:
            pyexif.Exif(self.fname_no_exif)
        self.assertEqual(
            'Image does not contain exif data',
            str(context.exception))

    def test_no_image(self):
        with self.assertRaises(IOError) as context:
            pyexif.Exif(self.fname_ioerror)
        self.assertEqual(
            'Can not find image',
            str(context.exception))

    def test_image_with_exif_data_northern_hemisphere(self):
        result = pyexif.Exif(self.fname_with_exif_northern_hemisphere)
        self.assertAlmostEqual(result.lat, 48.7390111111, delta=0.0001)
        self.assertAlmostEqual(result.lon, -113.749747222, delta=0.0001)

    def test_image_with_exif_data_southern_hemisphere(self):
        result = pyexif.Exif(self.fname_with_exif_southern_hemisphere)
        self.assertAlmostEqual(result.lat, -41.277833333333, delta=0.0001)
        self.assertAlmostEqual(result.lon, 174.777166666666, delta=0.0001)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
