import os
import json
from pathlib import Path
from dataclasses import dataclass, field

try:
    import yaml
except ImportError:
    yaml = None

@dataclass
class AgentConfig:
    display_name: str
    trigger: str
    slash: str
    aliases: list = field(default_factory=list)
    max_turns: int = 30

@dataclass
class Settings:
    app_name: str = "Raspy_Hermes"
    environment: str = "Kronos_School"
    max_attachment_size_mb: int = 10
    default_agent: str = "master"
    agents: dict = field(default_factory=dict)

    @classmethod
    def load(cls, config_path: str = None) -> "Settings":
        if not config_path:
            config_path = os.getenv("SETTINGS_PATH", "config/settings.yaml")
        
        path = Path(config_path)
        if not path.exists():
            return cls._default_settings()

        content = path.read_text(encoding="utf-8")
        data = {}
        if yaml:
            data = yaml.safe_load(content) or {}
        else:
            data = cls._simple_yaml_parse(content)

        app_data = data.get("app", {})
        agents_data = data.get("agents", {})

        parsed_agents = {}
        for name, cfg in agents_data.items():
            parsed_agents[name] = AgentConfig(
                display_name=cfg.get("display_name", name.title()),
                trigger=cfg.get("trigger", f"@{name.title()}"),
                slash=cfg.get("slash", f"/{name}"),
                aliases=cfg.get("aliases", []),
                max_turns=cfg.get("max_turns", 30)
            )

        return cls(
            app_name=app_data.get("name", "Raspy_Hermes"),
            environment=app_data.get("environment", "Kronos_School"),
            max_attachment_size_mb=app_data.get("max_attachment_size_mb", 10),
            default_agent=data.get("default_agent", "master"),
            agents=parsed_agents,
        )

    @classmethod
    def _default_settings(cls) -> "Settings":
        default_agents = {
            "capa": AgentConfig("Maestro Capa", "@Capa", "/capa", max_turns=30),
            "elektra": AgentConfig("Elektra / Chispa", "@Elektra", "/elektra", aliases=["@Chispa"], max_turns=25),
            "bio": AgentConfig("Bio", "@Bio", "/bio", max_turns=20),
            "caraxes": AgentConfig("Caraxes", "@Caraxes", "/caraxes", max_turns=35),
            "daemon": AgentConfig("Daemon", "@Daemon", "/daemon", max_turns=30),
            "warden": AgentConfig("Warden", "@Warden", "/warden", max_turns=25),
            "master": AgentConfig("Master", "@Master", "/master", max_turns=40),
            "tutor_conversion": AgentConfig("TutorConversion", "@TutorConversion", "/tutor_conversion", max_turns=35),
        }
        return cls(agents=default_agents)

    @staticmethod
    def _simple_yaml_parse(content: str) -> dict:
        # Fallback simple parser if PyYAML is not installed
        data = {"app": {"name": "Raspy_Hermes", "environment": "Kronos_School"}, "default_agent": "master", "agents": {}}
        current_section = None
        current_agent = None
        
        for line in content.splitlines():
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue
            
            if line_str == "app:":
                current_section = "app"
                continue
            elif line_str == "agents:":
                current_section = "agents"
                continue
            
            if current_section == "app" and ":" in line_str:
                k, v = line_str.split(":", 1)
                data["app"][k.strip()] = v.strip().strip('"').strip("'")
            elif current_section == "agents":
                if line.startswith("  ") and not line.startswith("    ") and line_str.endswith(":"):
                    current_agent = line_str[:-1]
                    data["agents"][current_agent] = {"aliases": []}
                elif current_agent and ":" in line_str:
                    k, v = line_str.split(":", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if k == "max_turns":
                        data["agents"][current_agent][k] = int(v)
                    elif k != "aliases":
                        data["agents"][current_agent][k] = v
        return data
