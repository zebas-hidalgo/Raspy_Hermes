[← Volver al README Principal](../../README.md) • [📖 Diccionario de Skills](diccionario_skills.md) • [🛡️ Seguridad](arquitectura_seguridad.md)

---

# 🔄 Ciclo de Vida de una Skill en Hermes Agent

Este documento detalla las 5 fases por las que pasa una habilidad (Skill) desde su concepción hasta su despliegue activo en el ecosistema **Raspy_Hermes**.

![Ciclo de Vida de una Skill](../../diagrams/ciclo_vida_skill.svg)

---

## 🚀 Fases del Proceso

### 1. Detección de Necesidad Educativa
- Identificación de un nuevo requerimiento en el laboratorio (un nuevo sensor en robótica, una técnica de reciclaje, una nueva guía docente).
- Recolección de casos de uso y preguntas frecuentes de los estudiantes.

### 2. Diseño y Especificación Arquitectónica (`@Caraxes`)
- `@Caraxes` estructura el modelo C4/D2 de la habilidad.
- Define el nombre único, trigger `/slash`, dependencias y límite de turnos.

### 3. Creación y Empaquetado `SKILL.md` (`@Daemon`)
- `@Daemon` genera el archivo `SKILL.md` con frontmatter YAML normalizado.
- Redacta las directrices de personalidad, ejemplos de entrada/salida y herramientas secundarias.

### 4. Auditoría y Control de Calidad (`@Warden`)
- Pruebas de ejecución en entorno seguro.
- Verificación del consumo de memoria y validación de prompts seguros.

### 5. Activación y Despliegue en Modo Bot
- La skill queda disponible para todos los estudiantes y docentes en Telegram y Discord mediante `@NombreBot`.

---

[← Volver al README Principal](../../README.md)
