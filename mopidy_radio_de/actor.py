from __future__ import unicode_literals

import pykka

from mopidy import backend

from .library import RadioDeLibraryProvider
from .playlists import RadioDePlaylistsProvider
from .api import RadioDeApi


def format_proxy(scheme, username, password, hostname, port):
    if hostname:
        # scheme must exists, so if None is give, we set default to http
        if not scheme:
            scheme = "http"
        # idem with port, default at 80
        if not port:
            port = 80
        # with authentification
        if username and password:
            return "%s://%s:%s@%s:%i" % (
                scheme, username, password, hostname, port)
        # ... or without
        else:
            return "%s://%s:%i" % (scheme, hostname, port)
    else:
        return None


class RadioDeBackend(pykka.ThreadingActor, backend.Backend):
    def __init__(self, config, audio):
        super(RadioDeBackend, self).__init__()

        self.config = config

        proxy = format_proxy(
            scheme=config['proxy']['scheme'],
            username=config['proxy']['username'],
            password=config['proxy']['password'],
            hostname=config['proxy']['hostname'],
            port=config['proxy']['port'])

        self.library = RadioDeLibraryProvider(backend=self)
        self.playlists = RadioDePlaylistsProvider(backend=self)
        self.api = RadioDeApi(
            language=self.config['radio-de']['language'],
            proxy=proxy)

        self.uri_schemes = ['radio-de']

    def on_start(self):
        self.playlists.refresh()

    def on_stop(self):
        pass
