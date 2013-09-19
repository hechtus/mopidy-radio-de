from __future__ import unicode_literals

import logging
import urlparse

from mopidy.models import Track
from mopidy.backends import base
from mopidy.models import SearchResult

logger = logging.getLogger('mopidy.backends.radio')

class RadioLibraryProvider(base.BaseLibraryProvider):

    def find_exact(self, query=None, uris=None):
        return self.search(query, uris)

    def lookup(self, uri):
        station = self.backend.session.get_station_by_station_id(int(uri.split(':')[1]))
        return [self._station_to_track(station)]

    def refresh(self, uri=None):
        pass

    def search(self, query=None, uris=None):
        if query is None:
            return
        stations = []
        for (field, values) in query.iteritems():
            if hasattr(values, '__iter__'):
                values = ' '.join(values)

            if field == 'any':
                stations = self.backend.session.search_stations_by_string(values)

        return SearchResult(uri = 'radio:search',
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
            uri = 'radio:' + str(station['id']),
            name = station['name'],
            bitrate = station['bitrate'])
