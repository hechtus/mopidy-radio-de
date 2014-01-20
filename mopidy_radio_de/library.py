from __future__ import unicode_literals

import logging
import urlparse
from dateutil import parser

from mopidy import backend
from mopidy.models import SearchResult, Track

logger = logging.getLogger(__name__)


class RadioDeLibraryProvider(backend.LibraryProvider):

    def lookup(self, uri):
        station_id = int(urlparse.urlparse(uri).netloc)
        station = self.backend.api.get_station_by_station_id(station_id)
        return self._station_to_tracks(station)

    def search(self, query=None, uris=None):
        if query is None:
            return
        stations = []
        for (field, values) in query.iteritems():
            if field == 'any':
                if hasattr(values, '__iter__'):
                    values = ' '.join(values)

                stations += self.backend.api.search_stations_by_string(values)

        tracks = [self._station_to_track(station) for station in stations]
        return SearchResult(uri='radio-de:search', tracks=tracks)

    def _validate_query(self, query):
        for (_, values) in query.iteritems():
            if not values:
                raise LookupError('Missing query')
            for value in values:
                if not value:
                    raise LookupError('Missing query')

    def _station_to_track(self, station):
        return Track(
            uri='radio-de://' + str(station['id']),
            name=station['name'],
            bitrate=station['bitrate'])

    def _station_to_tracks(self, station):
        if station['podcastUrls']:
            tracks = []
            for track in station['podcastUrls']:
                if track['streamStatus'] == 'VALID':
                    name = station['name'] + ': ' + track['title']
                    date = parser.parse(track['published']).date().isoformat()
                    tracks.append(Track(uri=track['streamUrl'],
                                        name=name,
                                        date=date,
                                        bitrate=track['bitRate']))
            return tracks

        for suffix in ['m3u', 'pls']:
            if station['streamURL'].lower().endswith(suffix):
                url = self.backend.api.parse_playlist(station['streamURL'])
                if url:
                    return [Track(uri=url,
                                  name=station['name'],
                                  bitrate=station['bitrate'])]

        if station['streamUrls'][0]['streamStatus'] == 'VALID':
            return [Track(uri=station['streamUrls'][0]['streamUrl'],
                          name=station['name'],
                          bitrate=station['streamUrls'][0]['bitRate'])]
        else:
            return []
