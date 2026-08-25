# Raspy_Hermes

Documentación del funcionamiento de los agents/bots en modo bot para el entorno educativo Kronos_School.

## Visión General

Este repositorio contiene la documentación detallada de los 8 agents autónomos que componen el ecosistema de Hermes Agent en Kronos_School, diseñados para apoyar la enseñanza y aprendizaje en 6to grado básico (Chile) mediante interacción en plataformas de mensajería (Telegram, Discord, etc.) usando menciones `@Agent`.

## Estructura de los Agents

Los agents están organizados en 3 clusters funcionales:

| Cluster | Agents | Función Principal |
|---------|--------|-------------------|
| **Dominio** | Capa (impresión 3D), Elektra (electrónica), Bio (bioplásticos) | Expertos en áreas temáticas específicas de STEM |
| **Infraestructura** | Caraxes (arquitectura de skills), Daemon (creación de skills), Warden (mantenimiento del sistema) | Responsables de la creación, gestión y salud del ecosistema de agents |
| **Orquestación** | Master (orquestación de agents), TutorConversion (conversión de tutors a agents) | Coordinan el trabajo entre agents y facilitan la evolución del sistema |

## Inicio Rápido

Para interactuar con los agents en modo bot:

1. Asegúrate de que el gateway de Hermes esté conectado a tu plataforma de mensajería (Telegram/Discord/etc.)
2. Usa la sintaxis `@NombreAgent <mensaje>` para dirigirte a un agent específico
3. Los agents responderán en el mismo hilo/chat con información relevante a su dominio

Ejemplo en Telegram:
```
@Capa ¿Cuál es la temperatura óptima para imprimir PLA en una Ender 3?
```
Respuesta:
```
Para PLA en una Ender 3, recomiendo:
- Temperatura del extrusor: 200-220°C
- Cama caliente: 50-60°C
- Velocidad de impresión: 50-60 mm/s
- Retracción: 5-7 mm a 25-40 mm/s
¿Necesitas ayuda con algún parámetro específico?
```

## Documentación Detallada

Consulta la carpeta `docs/` para documentación específica de cada agent:
- [Capa](docs/capa.md) - Maestro de impresión 3D
- [Elektra](docs/elektra.md) - Experta en electrónica
- [Bio](docs/bio.md) - Mentor de bioplásticos
- [Caraxes](docs/caraxes.md) - Arquitecto de skills
- [Daemon](docs/daemon.md) - Creador de skills
- [Warden](docs/warden.md) - Guardián del sistema
- [Master](docs/master.md) - Orquestador de agents
- [TutorConversion](docs/tutor_conversion.md) - Conversor de tutors

## Diagramas

Visita la carpeta `diagrams/` para visualizaciones de:
- Arquitectura de clusters de agents
- Flujos de interacción en modo bot
- Flujos de trabajo típicos por agent

## Recursos Adicionales

- `assets/ejemplos/` contiene configuraciones de ejemplo y comandos útiles
- Cada agent documenta sus skills principales y cómo usarlos en contexto educativo

## Contribución

Si deseas contribuir a la documentación o proponer mejoras, por favor abre un issue o pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---
*Documentación mantenida por el equipo de Kronos_School usando Hermes Agent.*
