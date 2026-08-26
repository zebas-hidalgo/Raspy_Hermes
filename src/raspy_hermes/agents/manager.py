from raspy_hermes.config import Settings, AgentConfig
from raspy_hermes.utils.logger import setup_logger

logger = setup_logger("agent_manager")

class AgentManager:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.agents: dict[str, AgentConfig] = settings.agents

    def get_agent(self, agent_id: str) -> AgentConfig:
        return self.agents.get(agent_id, self.agents.get(self.settings.default_agent))

    def list_agents(self) -> list[str]:
        return list(self.agents.keys())
