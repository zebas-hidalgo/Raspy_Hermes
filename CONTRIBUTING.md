# 🤝 Guía de Contribución a Raspy_Hermes

¡Gracias por tu interés en contribuir al ecosistema educativo de **Raspy_Hermes**! Este repositorio es un proyecto abierto diseñado para enriquecer el aprendizaje práctico STEM y Maker.

---

## 🌟 Formas de Contribuir

1. **Proponer una Nueva Habilidad (Skill):** Si desarrollaste una nueva actividad práctica (ej. robótica submarina, corte láser, compostaje escolar).
2. **Mejorar Guías Pedagógicas:** Agregar nuevos casos de uso ABP o adaptar objetivos de aprendizaje.
3. **Reportar Errores o Sugerir Diagramas:** Si encuentras inconsistencias en los esquemas técnicos o en los ejemplos.

---

## 🛠️ Flujo para Proponer una Nueva Skill (`SKILL.md`)

Para proponer una habilidad compatible con el motor de **Hermes Agent**:

1. **Estructura Requerida:** Crea un archivo `SKILL.md` con su correspondiente frontmatter YAML:
   ```yaml
   ---
   name: nombre_skill
   description: Descripción clara de cuándo y cómo el agente debe activar esta habilidad.
   ---
   ```
2. **Definir Directrices:** Incluye el rol, parámetros numéricos de seguridad y ejemplos de entrada/salida.
3. **Validación:** Consulta el documento [🔄 Ciclo de Vida de una Skill](docs/referencias/ciclo_vida_skills.md) y [🛡️ Arquitectura de Seguridad](docs/referencias/arquitectura_seguridad.md).

---

## 📜 Código de Conducta

Promovemos un entorno inclusivo, respetuoso y seguro para estudiantes, docentes y desarrolladores. Todas las interacciones deben mantener un tono constructivo y pedagógico.

---

[← Volver al README Principal](README.md)
