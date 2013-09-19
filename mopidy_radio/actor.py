from __future__ import unicode_literals

import pykka

from mopidy.backends import base

from .library import RadioLibraryProvider
from .playback import RadioPlaybackProvider
from .api import RadioApi

def do_nothing(*args, **kwargs):
    pass

class RadioBackend(pykka.ThreadingActor, base.Backend):
    def __init__(self, config, audio):
        super(RadioBackend, self).__init__()

        self.config = config

        self.library = RadioLibraryProvider(backend=self)
        self.playback = RadioPlaybackProvider(audio=audio, backend=self)
        self.session = RadioApi()
        self.session.log = do_nothing

        self.uri_schemes = ['radio']

    def on_start(self):
        pass

    def on_stop(self):
        pass
