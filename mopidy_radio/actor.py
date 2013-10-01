from __future__ import unicode_literals

import pykka

from mopidy.backends import base

from .library import RadioLibraryProvider
from .playlists import RadioPlaylistsProvider
from .api import RadioApi

class RadioBackend(pykka.ThreadingActor, base.Backend):
    def __init__(self, config, audio):
        super(RadioBackend, self).__init__()

        self.config = config

        self.library = RadioLibraryProvider(backend=self)
        self.playlists = RadioPlaylistsProvider(backend=self)
        self.session = RadioApi(language=self.config['radio']['language'])
        self.session.log = self.log

        self.uri_schemes = ['radio']

    def on_start(self):
        self.playlists.refresh()

    def on_stop(self):
        pass

    @staticmethod
    def log(text):
        pass
