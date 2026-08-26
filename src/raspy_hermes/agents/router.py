import re
from raspy_hermes.config import Settings

class MessageRouter:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._build_lookup()

    def _build_lookup(self):
        self.lookup = {}
        for agent_id, cfg in self.settings.agents.items():
            self.lookup[cfg.trigger.lower()] = agent_id
            self.lookup[cfg.slash.lower()] = agent_id
            for alias in cfg.aliases:
                self.lookup[alias.lower()] = agent_id

    def resolve_agent(self, text: str) -> str:
        if not text:
            return self.settings.default_agent

        first_word = text.strip().split()[0].lower() if text.strip() else ""
        if first_word in self.lookup:
            return self.lookup[first_word]

        for trigger, agent_id in self.lookup.items():
            if trigger in text.lower():
                return agent_id

        return self.settings.default_agent
