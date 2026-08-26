import unittest
from raspy_hermes.config import Settings
from raspy_hermes.agents.manager import AgentManager

class TestAgentManager(unittest.TestCase):
    def setUp(self):
        self.settings = Settings.load()
        self.manager = AgentManager(self.settings)

    def test_manager_loads_all_agents(self):
        agents = self.manager.list_agents()
        self.assertEqual(len(agents), 8)
        self.assertIn("capa", agents)
        self.assertIn("warden", agents)

    def test_get_agent_details(self):
        agent = self.manager.get_agent("elektra")
        self.assertEqual(agent.display_name, "Elektra / Chispa")

if __name__ == "__main__":
    unittest.main()
