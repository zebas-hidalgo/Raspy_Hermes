import unittest
from raspy_hermes.config import Settings
from raspy_hermes.agents.router import MessageRouter

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.settings = Settings.load()
        self.router = MessageRouter(self.settings)

    def test_route_mention_capa(self):
        agent_id = self.router.resolve_agent("@Capa ¿Cuál es la temperatura de PLA?")
        self.assertEqual(agent_id, "capa")

    def test_route_alias_chispa(self):
        agent_id = self.router.resolve_agent("@Chispa ¿Cómo conecto un LED?")
        self.assertEqual(agent_id, "elektra")

    def test_route_slash_bio(self):
        agent_id = self.router.resolve_agent("/bio Receta de almidón")
        self.assertEqual(agent_id, "bio")

    def test_route_default_fallback(self):
        agent_id = self.router.resolve_agent("Hola equipo, necesitamos ayuda")
        self.assertEqual(agent_id, "master")

if __name__ == "__main__":
    unittest.main()
