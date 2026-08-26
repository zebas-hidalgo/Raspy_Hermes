# Especificación de Diseño: Código Base Completo de Raspy_Hermes

**Fecha:** 2026-08-26  
**Autor:** Equipo Antigravity / Kronos_School  
**Estado:** Propuesto (Para Revisión)

---

## 1. Visión General y Objetivos

Convertir el repositorio `Raspy_Hermes` de un repositorio puramente documental a una **plataforma ejecutable completa y modular** en Python que gestione la red de 8 agentes autónomos para Kronos_School.

### Objetivos Principales:
1. Proporcionar un motor gateway ejecutable en Python (`src/raspy_hermes/`) compatible con Telegram y Discord.
2. Implementar un router de mensajes inteligente que parsee sintaxis `@NombreAgent` y comandos slash (`/capa`, `/elektra`, etc.).
3. Crear las 8 definiciones de habilidades (`skills/*/SKILL.md`) con estándares nativos de Hermes Agent.
4. Proveer soporte para despliegue simplificado en Raspberry Pi o servidores mediante `docker-compose.yml`, `Dockerfile` y `.env.example`.
5. Incluir una suite de pruebas unitarias con `pytest` para garantizar el correcto funcionamiento del enrutamiento y la carga de agentes.

---

## 2. Arquitectura del Sistema

```
                        +-----------------------------------+
                        |   Estudiantes & Docentes (Chat)   |
                        +-----------------------------------+
                                          |
                                          v
                        +-----------------------------------+
                        |  Gateway (Telegram / Discord API) |
                        +-----------------------------------+
                                          |
                                          v
                        +-----------------------------------+
                        |    Message Router (sintaxis @)    |
                        +-----------------------------------+
                                          |
                                          v
                        +-----------------------------------+
                        |   Agent Manager (8 Agentes)       |
                        +-----------------------------------+
                                          |
                 +------------------------+------------------------+
                 |                        |                        |
                 v                        v                        v
        [Cluster Dominio]        [Cluster Infraestructura]  [Cluster Orquestación]
        • Capa                   • Caraxes                  • Master
        • Elektra                • Daemon                   • TutorConversion
        • Bio                    • Warden
                 |                        |                        |
                 +------------------------+------------------------+
                                          |
                                          v
                        +-----------------------------------+
                        |   Hermes Skill Engine & LLM API   |
                        +-----------------------------------+
```

---

## 3. Estructura de Directorios

```
Raspy_Hermes/
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── config/
│   └── settings.yaml
├── src/
│   └── raspy_hermes/
│       ├── __init__.py
│       ├── main.py                # Entrypoint CLI
│       ├── config.py              # Gestión de entorno
│       ├── gateway/
│       │   ├── __init__.py
│       │   ├── base.py            # Clase base de gateway
│       │   └── telegram_gateway.py # Conector Telegram Bot API
│       ├── agents/
│       │   ├── __init__.py
│       │   ├── manager.py         # Registro de los 8 agentes
│       │   └── router.py          # Parser de @Agent y /slash
│       └── utils/
│           ├── __init__.py
│           └── logger.py
├── skills/
│   ├── capa/SKILL.md
│   ├── elektra/SKILL.md
│   ├── bio/SKILL.md
│   ├── caraxes/SKILL.md
│   ├── daemon/SKILL.md
│   ├── warden/SKILL.md
│   ├── master/SKILL.md
│   └── tutor_conversion/SKILL.md
├── docs/
│   └── ...
├── diagrams/
│   └── ...
└── tests/
    ├── test_router.py
    └── test_agent_manager.py
```

---

## 4. Definición de Componentes

### 4.1 `src/raspy_hermes/config.py`
Gestión de variables de entorno (`.env`) como tokens de bot (`TELEGRAM_BOT_TOKEN`, `DISCORD_BOT_TOKEN`), proveedor LLM (`HERMES_MODEL`, `HERMES_PROVIDER`), y umbrales de compresión.

### 4.2 `src/raspy_hermes/agents/router.py`
Detecta cuál de los 8 agentes debe procesar el mensaje:
- Si el mensaje incluye `@Capa` o inicia con `/capa` -> enruta a `CapaAgent`.
- Si incluye `@Elektra` o `@Chispa` o `/elektra` -> enruta a `ElektraAgent`.
- De manera similar para los demás agentes. Si no hay mención explícita, enruta por defecto a `MasterAgent`.

### 4.3 `skills/<agente>/SKILL.md`
Definiciones de prompts de sistema, herramientas asociadas, restricciones pedagógicas y ejemplos de uso para cada uno de los 8 agentes.

### 4.4 `docker-compose.yml`
Permite levantar la red completa de bots con un solo comando:
```bash
docker compose up -d
```

---

## 5. Plan de Pruebas y Verificación

1. **Pruebas Unitarias (`pytest`):**
   - Verificar enrutamiento correcto para los 8 agentes y sus alias (`@Chispa`, `/bio`, etc.).
   - Verificación de parseo de configuraciones `.env`.
   - Carga correcta de las 8 definiciones de `SKILL.md`.
2. **Prueba de Ejecución CLI:**
   - Probar comando `python -m raspy_hermes.main --dry-run` para validar inicialización limpia.
