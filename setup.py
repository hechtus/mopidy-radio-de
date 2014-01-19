from __future__ import unicode_literals

import re
from setuptools import setup, find_packages


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']

setup(
    name='Mopidy-radio-de',
    version=get_version('mopidy_radio_de/__init__.py'),
    url='http://github.com/hechtus/mopidy-radio-de/',
    license='Apache License, Version 2.0',
    author='Ronald Hecht',
    author_email='ronald.hecht@gmx.de',
    description='radio.de extension for Mopidy',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 0.18',
        'Pykka >= 1.1',
        'python-dateutil',
    ],
    entry_points={
        'mopidy.ext': [
            'radio-de = mopidy_radio_de:RadioDeExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
