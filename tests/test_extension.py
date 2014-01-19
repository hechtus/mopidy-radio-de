import mock
import unittest

from mopidy_radio_de import RadioDeExtension, actor as backend_lib


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

    def test_setup(self):
        registry = mock.Mock()

        ext = RadioDeExtension()
        ext.setup(registry)

        registry.add.assert_called_once_with(
            'backend', backend_lib.RadioDeBackend)
