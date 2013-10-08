from __future__ import unicode_literals

import logging
import urlparse
import dateutil

from mopidy.models import Track
from mopidy.backends import base
from mopidy.models import SearchResult

logger = logging.getLogger('mopidy.backends.radio-de')

class RadioDeLibraryProvider(base.BaseLibraryProvider):

    def lookup(self, uri):
        station_id = int(urlparse.urlparse(uri).netloc)
        station = self.backend.session.get_station_by_station_id(station_id)
        return self._station_to_tracks(station)

    def search(self, query=None, uris=None):
        if query is None:
            return
        stations = []
        for (field, values) in query.iteritems():
            if field == 'any':
                if hasattr(values, '__iter__'):
                    values = ' '.join(values)

                stations += self.backend.session.search_stations_by_string(values)

        return SearchResult(uri = 'radio-de:search',
                            tracks = [self._station_to_track(station) for station in stations])

    def _validate_query(self, query):
        for (_, values) in query.iteritems():
            if not values:
                raise LookupError('Missing query')
            for value in values:
                if not value:
                    raise LookupError('Missing query')

    def _station_to_track(self, station):
        return Track(
            uri = 'radio-de://' + str(station['id']),
            name = station['name'],
            bitrate = station['bitrate'])

    def _station_to_tracks(self, station):
        if station['podcastUrls']:
            tracks = []
            for track in station['podcastUrls']:
                if track['streamStatus'] == 'VALID':
                    tracks.append(Track(uri = track['streamUrl'],
                                        name = station['name'] + ': ' + track['title'],
                                        date = dateutil.parser.parse(track['published']).date().isoformat(),
                                        bitrate = track['bitRate']))
            return tracks

        for suffix in ['m3u', 'pls']:
            if station['streamURL'].lower().endswith(suffix):
                url = self.backend.session.parse_playlist(station['streamURL'])
                if url:
                    return [Track(uri = url,
                                  name = station['name'],
                                  bitrate = station['bitrate'])]
        
        if station['streamUrls'][0]['streamStatus'] == 'VALID':
            return [Track(uri = station['streamUrls'][0]['streamUrl'],
                          name = station['name'],
                          bitrate = station['streamUrls'][0]['bitRate'])]
        else:
            return []
