from __future__ import unicode_literals

from mopidy.backends import base


class RadioPlaybackProvider(base.BasePlaybackProvider):

    def play(self, track):
        station = self.backend.session.get_station_by_station_id(track.uri.split(':')[1])
        self.audio.prepare_change()
        self.audio.set_uri(station['stream_url']).get()
        return self.audio.start_playback().get()
