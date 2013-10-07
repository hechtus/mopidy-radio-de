from __future__ import unicode_literals

import pykka

from mopidy.backends import base

from .library import RadioDeLibraryProvider
from .playlists import RadioDePlaylistsProvider
from .api import RadioDeApi

class RadioDeBackend(pykka.ThreadingActor, base.Backend):
    def __init__(self, config, audio):
        super(RadioDeBackend, self).__init__()

        self.config = config

        self.library = RadioDeLibraryProvider(backend=self)
        self.playlists = RadioDePlaylistsProvider(backend=self)
        self.session = RadioDeApi(language=self.config['radio-de']['language'])
        self.session.log = self.log

        self.uri_schemes = ['radio-de']

    def on_start(self):
        self.playlists.refresh()

    def on_stop(self):
        pass

    @staticmethod
    def log(text):
        pass
