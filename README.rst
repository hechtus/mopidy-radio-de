***************
Mopidy-radio-de
***************

.. image:: https://pypip.in/v/Mopidy-radio-de/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-radio-de/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/Mopidy-radio-de/badge.png
    :target: https://pypi.python.org/pypi/Mopidy-radio-de/
    :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/hechtus/mopidy-radio-de.png?branch=master
    :target: https://travis-ci.org/hechtus/mopidy-radio-de
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/hechtus/mopidy-radio-de/badge.png?branch=master
   :target: https://coveralls.io/r/hechtus/mopidy-radio-de?branch=master
   :alt: Test coverage

`Mopidy <http://www.mopidy.com/>`_ extension to listen to internet
radio stations and podcasts listed at `radio.de
<http://www.radio.de/>`_, `rad.io <http://www.rad.io/>`_, `radio.fr
<http://www.radio.fr/>`_, and `radio.at <http://www.radio.at/>`_.


Installation
============

Install the Mopidy-radio-de extension by running::

    pip install mopidy-radio-de


Configuration
=============

Before starting Mopidy, you must select your preferred language in the
Mopidy configuration file. This will affect the stations and podcasts
being found. Choose between german, austrian, french, and english. You
can also optionally define favorite stations that will appear as
playlists::

    [radio-de]
    language = german
    favorites = Tagesschau, NDR 2, NDR Kultur


Usage
=====

The extension is enabled by default. You can search for radio stations
and listen to them.


Project resources
=================

- `Source code <https://github.com/hechtus/mopidy-radio-de>`_
- `Issue tracker <https://github.com/hechtus/mopidy-radio-de/issues>`_
- `Download development snapshot
  <https://github.com/hechtus/mopidy-radio-de/archive/master.zip>`_


Changelog
=========

v0.2.0 (2014-02-17)
-------------------

- Require Mopidy >= 0.18.0.
- Added proxy support


v0.1.3 (2013-12-02)
-------------------

- Issue #4: Fixed a problem regarding favorites. Some stations could
  not be found by the plugin.


v0.1.2 (2013-11-08)
-------------------

- Added python-dateutil dependency
- Added Travis CI and coveralls support


v0.1.1 (2013-10-08)
-------------------

- Extension renamed to Mopidy-radio-de
- Added austrian support
- Minor clean-up of library code


v0.1 (2013-10-07)
-----------------

- Initial release
