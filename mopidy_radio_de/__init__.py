from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '0.2.0'


class RadioDeExtension(ext.Extension):

    dist_name = 'Mopidy-radio-de'
    ext_name = 'radio-de'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(RadioDeExtension, self).get_config_schema()
        schema['language'] = config.String()
        schema['favorites'] = config.List(optional=True)
        return schema

    def setup(self, registry):
        from .actor import RadioDeBackend
        registry.add('backend', RadioDeBackend)
