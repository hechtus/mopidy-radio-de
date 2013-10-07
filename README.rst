Mopidy-Radio-de
===============

`Mopidy <http://www.mopidy.com/>`_ extension to listen to internet
radio stations and podcasts from `radio.de <http://www.radio.de/>`_,
`rad.io <http://www.rad.io/>`_, `radio.fr <http://www.radio.fr/>`_,
and `radio.at <http://www.radio.at/>`_.


Usage
-----

#. Install the Mopidy-Radio-de extension by running::

    pip install mopidy-radio-de
   
#. Before starting Mopidy, you must select your preferred language in
   the Mopidy configuration file. This will affect the stations and
   podcasts being found. Choose between german, austrian, french, and
   english. You can also optionally define favorite stations that will
   appear as playlists::

    [radio-de]
    language = german
    favorites = Tagesschau, NDR 2, NDR Kultur

Project resources
-----------------

- `Source code <https://github.com/hechtus/mopidy-radio-de>`_
- `Issue tracker <https://github.com/hechtus/mopidy-radio-de/issues>`_
- `Download development snapshot
  <https://github.com/hechtus/mopidy-radio-de/archive/master.zip>`_
