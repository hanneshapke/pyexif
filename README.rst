===============================
PyEXIF
===============================

.. image:: https://badge.fury.io/py/pyexif.png
    :target: http://badge.fury.io/py/pyexif

.. image:: https://travis-ci.org/hanneshapke/pyexif.png?branch=master
    :target: https://travis-ci.org/hanneshapke/pyexif

.. image:: https://coveralls.io/repos/hanneshapke/pyexif/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/hanneshapke/pyexif?branch=master



Read EXIF from jpegs.

* Free software: BSD license
* Documentation: https://pyexif.readthedocs.org.

How to use the package
--------

* Install package

* Run the following code

.. code-block:: python
:linenos:
  #!/usr/bin/python
"""Sample code to demonstrate pyexif"""
from pyexif.pyexif import Exif
file_name = “your_image.JPG"
result = Exif.load_image(file_name)
print ("The available attributes are: %s" % result.gps_attributes)
print ("Your location: %s %s" % result.lat, result.lon)


Further Readings
----------------
Exif sepcs:
http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf


Thanks to
--------
The works was inspired by
erans: https://gist.github.com/erans/983821
Daniel Brown: http://www.endlesslycurious.com/2011/05/11/extracting-image-exif-data-with-python/
