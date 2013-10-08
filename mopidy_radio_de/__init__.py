from __future__ import unicode_literals

import os

import mopidy
from mopidy import config, exceptions, ext


__version__ = '0.1.1'


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

    def validate_environment(self):
        pass

    def get_backend_classes(self):
        from .actor import RadioDeBackend
        return [RadioDeBackend]
