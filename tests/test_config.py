import unittest
from raspy_hermes.config import Settings

class TestConfig(unittest.TestCase):
    def test_load_default_settings(self):
        settings = Settings.load()
        self.assertEqual(settings.app_name, "Raspy_Hermes")
        self.assertIn("capa", settings.agents)
        self.assertEqual(settings.agents["capa"].trigger, "@Capa")
        self.assertEqual(settings.agents["capa"].slash, "/capa")

    def test_custom_settings_fallback(self):
        settings = Settings.load("non_existent.yaml")
        self.assertEqual(settings.app_name, "Raspy_Hermes")
        self.assertEqual(settings.default_agent, "master")

if __name__ == "__main__":
    unittest.main()
