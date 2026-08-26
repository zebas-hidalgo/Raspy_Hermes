[← Volver al README Principal](../../README.md) • [📚 Glosario](glosario_stem.md) • [📖 Diccionario de Skills](diccionario_skills.md)

---

# 🛡️ Arquitectura de Seguridad, Filtrado y Sandbox Educativo

Este documento describe los mecanismos de seguridad multicapa implementados en **Raspy_Hermes** para garantizar una experiencia de aprendizaje segura para los estudiantes y proteger la infraestructura del laboratorio.

![Arquitectura de Seguridad](../../diagrams/seguridad_sandbox.svg)

---

## 🔒 Capas de Protección

### 1. Sanitización de Entrada (Ingestion Layer)
- **Validación de Archivos:** El sistema restringe la carga de adjuntos a formatos seguros (`.stl`, `.obj`, `.3mf`, `.png`, `.jpg`, `.pdf`, `.ino`). Archivos ejecutables (`.exe`, `.sh`, `.bat`) son bloqueados automáticamente.
- **Límite de Tamaño:** Máximo de 10 MB por archivo adjunto para prevenir sobrecarga de red y almacenamiento.
- **Protección Anti-Prompt Injection:** Los prompts de los usuarios son aislados en el rol de `user`, preservando invariables las directrices pedagógicas y de seguridad del `system_prompt`.

### 2. Aislamiento y Control de Recursos (Sandbox Layer)
- **Control de Turnos:** Cada agente tiene un límite máximo de turnos de conversación configurado en `config/settings.yaml` (entre 20 y 40 turnos).
- **Monitoreo Warden:** El agente `@Warden` vigila continuamente el uso de memoria RAM y CPU en el contenedor Docker.

### 3. Seguridad de Contenido y Física (Pedagogical Safety)
- **Check de Voltajes:** `@Elektra` valida que los diagramas de circuitos operen bajo voltajes seguros (< 12V DC) y contengan resistencias limitadoras para proteger componentes.
- **Advertencias de Proceso:** `@Bio` y `@Capa` incluyen avisos de precaución al manipular boquillas calientes (200°C) o fuentes de calor para bioplásticos.

---

[← Volver al README Principal](../../README.md)
