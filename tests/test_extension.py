import unittest

from mopidy_radio-de import RadioDeExtension, actor as backend_lib


class ExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = RadioDeExtension()

        config = ext.get_default_config()

        self.assertIn('[radio-de]', config)
        self.assertIn('enabled = true', config)

    def test_get_config_schema(self):
        ext = RadioDeExtension()

        schema = ext.get_config_schema()

        self.assertIn('favorites', schema)

    def test_get_backend_classes(self):
        ext = RadioDeExtension()

        backends = ext.get_backend_classes()

        self.assertIn(backend_lib.RadioDeBackend, backends)
