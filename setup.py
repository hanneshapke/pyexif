#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Pillow',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='pyexif',
    version='0.1.0',
    description='Read EXIF from jpegs.',
    long_description=readme + '\n\n' + history,
    author='Hannes Hapke',
    author_email='hannes.hapke@gmail.com',
    url='https://github.com/hanneshapke/pyexif',
    download_url='https://github.com/hanneshapke/pyexif',
    license="The MIT License",
    packages=[
        'pyexif',
    ],
    package_dir={'pyexif':
                 'pyexif'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='pyexif',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
