# Raspy_Hermes

Documentación del funcionamiento de los agentes/bots autónomos en modo bot para el entorno educativo **Kronos_School**.

---

## 🌟 Visión General

Este repositorio contiene la documentación detallada y la arquitectura de diagramas vectoriales (SVG) de los 8 agentes autónomos que componen el ecosistema de **Hermes Agent** en Kronos_School, diseñados para apoyar la enseñanza y aprendizaje en 6to grado básico (Chile) mediante interacción en plataformas de mensajería (Telegram, Discord, etc.) utilizando menciones `@Agent`.

![Ecosistema General de Agentes](diagrams/ecosistema_general.svg)

---

## 🏗️ Estructura de Agentes por Clusters

Los agentes están organizados en 3 clusters funcionales:

| Cluster | Agente | Rol Principal | Documentación | Diagrama Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Dominio** | **Capa** | Maestro de Impresión 3D, STL & Cero Residuos | [Ver Doc](docs/capa.md) | ![Flujo Capa](diagrams/capa_flujo.svg) |
| | **Elektra / Chispa** | Experta en Electrónica & Microcontroladores | [Ver Doc](docs/elektra.md) | ![Flujo Elektra](diagrams/elektra_flujo.svg) |
| | **Bio** | Mentor de Bioplásticos & Química Verde | [Ver Doc](docs/bio.md) | ![Flujo Bio](diagrams/bio_flujo.svg) |
| **Infraestructura** | **Caraxes** | Arquitecto de Skills & Modelado C4/D2 | [Ver Doc](docs/caraxes.md) | ![Flujo Caraxes](diagrams/caraxes_flujo.svg) |
| | **Daemon** | Creador & Mantenedor de Skills | [Ver Doc](docs/daemon.md) | ![Flujo Daemon](diagrams/daemon_flujo.svg) |
| | **Warden** | Guardián del Sistema, Monitoreo & Seguridad | [Ver Doc](docs/warden.md) | ![Flujo Warden](diagrams/warden_flujo.svg) |
| **Orquestación** | **Master** | Orquestador de Proyectos Multidisciplinarios | [Ver Doc](docs/master.md) | ![Flujo Master](diagrams/master_flujo.svg) |
| | **TutorConversion** | Conversor Pedagógico de Tutors a Bots | [Ver Doc](docs/tutor_conversion.md) | ![Flujo TutorConversion](diagrams/tutor_conversion_flujo.svg) |

---

## 💬 Modo de Uso en Bot

Para interactuar con los agentes en plataformas de mensajería (Telegram/Discord):

1. Asegúrate de que el gateway de Hermes esté conectado a tu canal/grupo.
2. Utiliza la sintaxis `@NombreAgent <mensaje>` o comandos `/slash` para dirigirte a un agente específico.

### Ejemplos en Telegram:

- **@Capa**: `@Capa ¿Cuál es la temperatura recomendada para PLA en una Ender 3?`
- **@Elektra**: `@Elektra Genera el código de Arduino para leer un sensor LDR`
- **@Bio**: `@Bio ¿Cómo preparo bioplástico de almidón de maíz en clase?`
- **@Master**: `@Master Queremos hacer un proyecto de Ciudad Sostenible, ¿cómo coordinamos los equipos?`

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.
