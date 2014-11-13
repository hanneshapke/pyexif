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
        self.fname_with_exif = '/'.join(
            [BASE_DIR, 'glacier_national_park.jpg']
        )
        return self

    def test_image_without_exif_data(self):
        data = pyexif.get_exif_data(self.fname_no_exif)
        result = pyexif.get_lat_lon(data)
        self.assertEqual(result, False)

    def test_image_with_exif_data(self):
        data = pyexif.get_exif_data(self.fname_with_exif)
        result = pyexif.get_lat_lon(data)
        self.assertAlmostEqual(result[0], 48.7390111111)
        self.assertAlmostEqual(result[1], -113.74974722222)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
