Mopidy-Radio
=============

`Mopidy <http://www.mopidy.com/>`_ extension to listen to internet
radio stations and podcasts from `radio.de <http://www.radio.de/>`_.


Usage
-----

#. Install the Mopidy-Radio extension by running::

    sudo pip install mopidy-radio
   
#. Before starting Mopidy, you must select your preferred language in
   the Mopidy configuration file. This will affect the stations and
   podcasts being found. Choose between german, french, and
   english. You can also optionally define favorite stations that will
   appear as playlists::

    [radio]
    language = german
    favorites = Tagesschau, NDR 2, NDR Kultur

Project resources
-----------------

- `Source code <https://github.com/hechtus/mopidy-radio>`_
- `Issue tracker <https://github.com/hechtus/mopidy-radio/issues>`_
- `Download development snapshot
  <https://github.com/hechtus/mopidy-radio/archive/master.zip>`_
