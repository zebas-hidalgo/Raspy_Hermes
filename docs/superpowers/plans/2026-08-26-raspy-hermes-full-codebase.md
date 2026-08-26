# Raspy_Hermes Full Codebase Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir e integrar el paquete ejecutable completo de Raspy_Hermes (gateway Telegram, router de mensajes con sintaxis @, 8 skills nativas de Hermes Agent, Docker y suite de pruebas pytest).

**Architecture:** Paquete modular en `src/raspy_hermes/` respaldado por definiciones de habilidades en `skills/` e interfaz gateway para mensajería escolar.

**Tech Stack:** Python 3.10+, python-telegram-bot / httpx, pytest, PyYAML, Docker, Docker Compose.

---

## Map of Files to Create

```
skills/
├── capa/SKILL.md
├── elektra/SKILL.md
├── bio/SKILL.md
├── caraxes/SKILL.md
├── daemon/SKILL.md
├── warden/SKILL.md
├── master/SKILL.md
└── tutor_conversion/SKILL.md

src/raspy_hermes/
├── __init__.py
├── main.py
├── config.py
├── gateway/
│   ├── __init__.py
│   ├── base.py
│   └── telegram_gateway.py
├── agents/
│   ├── __init__.py
│   ├── manager.py
│   └── router.py
└── utils/
    ├── __init__.py
    └── logger.py

config/
└── settings.yaml

tests/
├── __init__.py
├── test_config.py
├── test_router.py
└── test_agent_manager.py

requirements.txt
pyproject.toml
Dockerfile
docker-compose.yml
.env.example
```

---

### Task 1: Project Setup & Package Configuration

**Files:**
- Create: `requirements.txt`
- Create: `pyproject.toml`
- Create: `.env.example`
- Create: `Dockerfile`
- Create: `docker-compose.yml`
- Create: `config/settings.yaml`

- [ ] **Step 1: Write requirements.txt**

```txt
python-telegram-bot>=20.0
pyyaml>=6.0
pydantic>=2.0
python-dotenv>=1.0.0
pytest>=7.0.0
httpx>=0.24.0
```

- [ ] **Step 2: Write pyproject.toml**

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "raspy-hermes"
version = "0.1.0"
description = "Ecosistema de 8 agentes autónomos para Kronos_School"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "python-telegram-bot>=20.0",
    "pyyaml>=6.0",
    "pydantic>=2.0",
    "python-dotenv>=1.0.0",
    "httpx>=0.24.0",
]

[project.scripts]
raspy-hermes = "raspy_hermes.main:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

- [ ] **Step 3: Write .env.example**

```env
TELEGRAM_BOT_TOKEN=tu_token_aqui
DISCORD_BOT_TOKEN=
HERMES_MODEL=nvidia/nemotron-3-super-120b-a12b
HERMES_PROVIDER=nvidia
LOG_LEVEL=INFO
SETTINGS_PATH=config/settings.yaml
```

- [ ] **Step 4: Write Dockerfile and docker-compose.yml**

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt pyproject.toml /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN pip install --no-cache-dir -e .

CMD ["python", "-m", "raspy_hermes.main"]
```

```yaml
version: '3.8'

services:
  raspy-hermes:
    build: .
    container_name: raspy_hermes_bot
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - ./config:/app/config
      - ./skills:/app/skills
```

- [ ] **Step 5: Write config/settings.yaml**

```yaml
app:
  name: "Raspy_Hermes"
  environment: "Kronos_School"
  max_attachment_size_mb: 10

default_agent: "master"

agents:
  capa:
    display_name: "Maestro Capa"
    trigger: "@Capa"
    slash: "/capa"
    max_turns: 30
  elektra:
    display_name: "Elektra / Chispa"
    trigger: "@Elektra"
    aliases: ["@Chispa"]
    slash: "/elektra"
    max_turns: 25
  bio:
    display_name: "Bio"
    trigger: "@Bio"
    slash: "/bio"
    max_turns: 20
  caraxes:
    display_name: "Caraxes"
    trigger: "@Caraxes"
    slash: "/caraxes"
    max_turns: 35
  daemon:
    display_name: "Daemon"
    trigger: "@Daemon"
    slash: "/daemon"
    max_turns: 30
  warden:
    display_name: "Warden"
    trigger: "@Warden"
    slash: "/warden"
    max_turns: 25
  master:
    display_name: "Master"
    trigger: "@Master"
    slash: "/master"
    max_turns: 40
  tutor_conversion:
    display_name: "TutorConversion"
    trigger: "@TutorConversion"
    slash: "/tutor_conversion"
    max_turns: 35
```

- [ ] **Step 6: Commit**

```bash
git add requirements.txt pyproject.toml .env.example Dockerfile docker-compose.yml config/settings.yaml
git commit -m "chore: setup project structure, dependencies, docker, and settings"
```

---

### Task 2: Config & Logger Module

**Files:**
- Create: `src/raspy_hermes/__init__.py`
- Create: `src/raspy_hermes/utils/__init__.py`
- Create: `src/raspy_hermes/utils/logger.py`
- Create: `src/raspy_hermes/config.py`
- Test: `tests/test_config.py`

- [ ] **Step 1: Write tests/test_config.py**

```python
import os
from raspy_hermes.config import Settings

def test_load_default_settings():
    settings = Settings.load()
    assert settings.app_name == "Raspy_Hermes"
    assert "capa" in settings.agents
    assert settings.agents["capa"].trigger == "@Capa"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_config.py`
Expected: FAIL (module raspy_hermes.config not found)

- [ ] **Step 3: Write src/raspy_hermes/utils/logger.py**

```python
import logging
import os

def setup_logger(name: str = "raspy_hermes") -> logging.Logger:
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(getattr(logging, level, logging.INFO))
    return logger
```

- [ ] **Step 4: Write src/raspy_hermes/config.py**

```python
import os
from pathlib import Path
import yaml
from pydantic import BaseModel, Field

class AgentConfig(BaseModel):
    display_name: str
    trigger: str
    aliases: list[str] = Field(default_factory=list)
    slash: str
    max_turns: int = 30

class Settings(BaseModel):
    app_name: str = "Raspy_Hermes"
    environment: str = "Kronos_School"
    max_attachment_size_mb: int = 10
    default_agent: str = "master"
    agents: dict[str, AgentConfig] = Field(default_factory=dict)

    @classmethod
    def load(cls, config_path: str = None) -> "Settings":
        if not config_path:
            config_path = os.getenv("SETTINGS_PATH", "config/settings.yaml")
        
        path = Path(config_path)
        if not path.exists():
            return cls()
            
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            
        app_data = data.get("app", {})
        agents_data = data.get("agents", {})
        
        parsed_agents = {
            name: AgentConfig(**cfg) for name, cfg in agents_data.items()
        }
        
        return cls(
            app_name=app_data.get("name", "Raspy_Hermes"),
            environment=app_data.get("environment", "Kronos_School"),
            max_attachment_size_mb=app_data.get("max_attachment_size_mb", 10),
            default_agent=data.get("default_agent", "master"),
            agents=parsed_agents,
        )
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_config.py`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/raspy_hermes/ tests/test_config.py
git commit -m "feat: add config and logger modules with tests"
```

---

### Task 3: Agent Router & Agent Manager

**Files:**
- Create: `src/raspy_hermes/agents/__init__.py`
- Create: `src/raspy_hermes/agents/manager.py`
- Create: `src/raspy_hermes/agents/router.py`
- Test: `tests/test_router.py`
- Test: `tests/test_agent_manager.py`

- [ ] **Step 1: Write failing tests for router and manager**

```python
# tests/test_router.py
from raspy_hermes.config import Settings
from raspy_hermes.agents.router import MessageRouter

def test_route_mention_capa():
    settings = Settings.load()
    router = MessageRouter(settings)
    
    agent_id = router.resolve_agent("@Capa ¿Cuál es la temperatura de PLA?")
    assert agent_id == "capa"

def test_route_alias_chispa():
    settings = Settings.load()
    router = MessageRouter(settings)
    
    agent_id = router.resolve_agent("@Chispa ¿Cómo conecto un LED?")
    assert agent_id == "elektra"

def test_route_slash_bio():
    settings = Settings.load()
    router = MessageRouter(settings)
    
    agent_id = router.resolve_agent("/bio Receta de almidón")
    assert agent_id == "bio"

def test_route_default_fallback():
    settings = Settings.load()
    router = MessageRouter(settings)
    
    agent_id = router.resolve_agent("Hola equipo, necesitamos ayuda")
    assert agent_id == "master"
```

```python
# tests/test_agent_manager.py
from raspy_hermes.config import Settings
from raspy_hermes.agents.manager import AgentManager

def test_manager_loads_all_agents():
    settings = Settings.load()
    manager = AgentManager(settings)
    agents = manager.list_agents()
    
    assert len(agents) == 8
    assert "capa" in agents
    assert "warden" in agents
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_router.py tests/test_agent_manager.py`
Expected: FAIL

- [ ] **Step 3: Write src/raspy_hermes/agents/router.py**

```python
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
```

- [ ] **Step 4: Write src/raspy_hermes/agents/manager.py**

```python
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
```

- [ ] **Step 5: Run test to verify it passes**

Run: `pytest tests/test_router.py tests/test_agent_manager.py`
Expected: PASS

- [ ] **Step 6: Commit**

```bash
git add src/raspy_hermes/agents/ tests/
git commit -m "feat: add message router and agent manager with unit tests"
```

---

### Task 4: Telegram Gateway & Main CLI Entrypoint

**Files:**
- Create: `src/raspy_hermes/gateway/__init__.py`
- Create: `src/raspy_hermes/gateway/base.py`
- Create: `src/raspy_hermes/gateway/telegram_gateway.py`
- Create: `src/raspy_hermes/main.py`

- [ ] **Step 1: Write src/raspy_hermes/gateway/base.py**

```python
from abc import ABC, abstractmethod

class BaseGateway(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
```

- [ ] **Step 2: Write src/raspy_hermes/gateway/telegram_gateway.py**

```python
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from raspy_hermes.config import Settings
from raspy_hermes.agents.router import MessageRouter
from raspy_hermes.agents.manager import AgentManager
from raspy_hermes.gateway.base import BaseGateway
from raspy_hermes.utils.logger import setup_logger

logger = setup_logger("telegram_gateway")

class TelegramGateway(BaseGateway):
    def __init__(self, settings: Settings):
        self.settings = settings
        self.token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.router = MessageRouter(settings)
        self.manager = AgentManager(settings)
        self.app = None

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.message or not update.message.text:
            return

        text = update.message.text
        agent_id = self.router.resolve_agent(text)
        agent = self.manager.get_agent(agent_id)

        logger.info(f"Mensaje recibido de {update.effective_user.name}: '{text}' -> Enrutado a {agent.display_name}")

        response = (
            f"🤖 *[{agent.display_name}]*\n\n"
            f"He recibido tu consulta sobre:_{text}_\n\n"
            f"Procesando en entorno Kronos_School (Turnos máx: {agent.max_turns})..."
        )
        await update.message.reply_text(response, parse_mode="Markdown")

    def start(self):
        if not self.token or self.token == "tu_token_aqui":
            logger.warning("TELEGRAM_BOT_TOKEN no configurado. Ejecutando en modo simulación/CLI.")
            return

        self.app = ApplicationBuilder().token(self.token).build()
        self.app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), self.handle_message))
        
        logger.info("Iniciando Gateway de Telegram...")
        self.app.run_polling()

    def stop(self):
        if self.app:
            self.app.stop()
```

- [ ] **Step 3: Write src/raspy_hermes/main.py**

```python
import argparse
import sys
from raspy_hermes.config import Settings
from raspy_hermes.gateway.telegram_gateway import TelegramGateway
from raspy_hermes.utils.logger import setup_logger

logger = setup_logger("main")

def main():
    parser = argparse.ArgumentParser(description="Raspy_Hermes Bot Runner")
    parser.add_argument("--dry-run", action="store_true", help="Validar configuración y salir")
    args = parser.parse_args()

    settings = Settings.load()
    logger.info(f"Cargado {settings.app_name} ({settings.environment}) con {len(settings.agents)} agentes.")

    if args.dry-run:
        logger.info("Modo dry-run finalizado con éxito.")
        sys.exit(0)

    gateway = TelegramGateway(settings)
    gateway.start()

if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Test CLI main dry-run**

Run: `python -m raspy_hermes.main --dry-run`
Expected: Output showing loaded settings and dry-run success.

- [ ] **Step 5: Commit**

```bash
git add src/raspy_hermes/gateway/ src/raspy_hermes/main.py
git commit -m "feat: add Telegram gateway interface and main CLI entrypoint"
```

---

### Task 5: 8 Native Hermes Skills Definitions

**Files:**
- Create: `skills/capa/SKILL.md`
- Create: `skills/elektra/SKILL.md`
- Create: `skills/bio/SKILL.md`
- Create: `skills/caraxes/SKILL.md`
- Create: `skills/daemon/SKILL.md`
- Create: `skills/warden/SKILL.md`
- Create: `skills/master/SKILL.md`
- Create: `skills/tutor_conversion/SKILL.md`

- [ ] **Step 1: Write all 8 SKILL.md files**
Write each file with proper frontmatter YAML name/description and detailed guidelines.

- [ ] **Step 2: Commit**

```bash
git add skills/
git commit -m "feat: add 8 native Hermes Agent skill definitions"
```

---

### Task 6: Push Clean Repository to GitHub Remote

**Files:**
- Modify/Remove old legacy files if any
- Push to GitHub origin/main

- [ ] **Step 1: Verify git status and run pytest**

Run: `pytest`
Expected: All tests PASS.

- [ ] **Step 2: Push clean main branch to GitHub**

Run: `git push origin main`
Expected: Clean push to `https://github.com/zebas-hidalgo/Raspy_Hermes.git`.
