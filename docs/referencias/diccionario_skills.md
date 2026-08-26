# 📚 Diccionario de Skills — Catálogo Técnico de Habilidades

Este diccionario actúa como la **referencia definitiva de habilidades (Skills)** para el ecosistema de **Hermes Agent** en Kronos_School. Cada habilidad está empaquetada mediante la especificación de archivos `SKILL.md` con su correspondiente frontmatter YAML y directrices operativas.

---

## 🗺️ Índice del Catálogo

| Skill ID | Agente Principal | Categoría | Propósito Principal |
| :--- | :--- | :--- | :--- |
| `capa` | `@Capa` | Dominio STEM | Asesoría en impresión 3D, laminado Slicer y filosofía cero residuos. |
| `elektra` | `@Elektra` | Dominio STEM | Asesoría en electrónica analógica/digital y código Arduino/ESP32. |
| `bio` | `@Bio` | Dominio STEM | Recetas de bioplásticos, química verde y economía circular. |
| `caraxes` | `@Caraxes` | Infraestructura | Especificación técnica de nuevas skills y modelado C4/D2. |
| `daemon` | `@Daemon` | Infraestructura | Creación, edición y validación de archivos `SKILL.md`. |
| `warden` | `@Warden` | Infraestructura | Monitoreo de memoria, salud del servidor y políticas de seguridad. |
| `master` | `@Master` | Orquestación | Coordinación de proyectos multidisciplinarios y delegación. |
| `tutor_conversion` | `@TutorConversion` | Orquestación | Transformación de guías PDF pasivas en bots tutores adaptativos. |

---

## 📋 Fichas Técnicas de Habilidades Nativas

### 🖨️ 1. `capa` — Maestro de Impresión 3D

```yaml
---
name: capa
description: Maestro especializado en Impresión 3D, diseño para manufactura aditiva, análisis de archivos STL y optimización cero residuos en Kronos_School. Usar cuando el usuario mencione @Capa o utilice /capa.
---
```

- **Entradas:** Texto de consulta, archivos `.STL`, `.OBJ`, `.3MF` o imágenes de fallas de impresión.
- **Herramientas Secundarias:** `stl_analyzer`, `slicer_profiles`, `excalidraw`.
- **Salida:** Parámetros de temperatura (°C), velocidad (mm/s), altura de capa (mm), densidad de relleno (%) y recomendaciones para evitar soportes innecesarios.
- **Ejemplo de Uso:**
  > `@Capa ¿Cuál es la temperatura de extrusión e infiltración recomendada para PLA en una Ender 3?`

---

### ⚡ 2. `elektra` — Experta en Electrónica & Microcontroladores

```yaml
---
name: elektra
description: Experta en electrónica analógica y digital, microcontroladores (Arduino/ESP32), prototipado en protoboard y circuitos seguros. Usar cuando el usuario mencione @Elektra, @Chispa o /elektra.
---
```

- **Entradas:** Requerimiento de circuito, lista de componentes o dudas de programación.
- **Herramientas Secundarias:** `ejemplo-codigo`, `diagnostico-bug`, `pdf-export`.
- **Salida:** Diagrama de conexiones en texto/ASCII, cálculo de resistencias con la Ley de Ohm y código `.ino` o `.py` comentado línea por línea.
- **Ejemplo de Uso:**
  > `@Elektra Genera el código para encender un LED RGB usando botones en Arduino.`

---

### 🌿 3. `bio` — Mentor de Bioplásticos & Sostenibilidad

```yaml
---
name: bio
description: Mentor curioso de bioplásticos, química verde, economía circular y materiales sostenibles escolares. Usar cuando el usuario mencione @Bio o /bio.
---
```

- **Entradas:** Consulta sobre materiales orgánicos o solicitud de recetas eco.
- **Herramientas Secundarias:** `recetario-bioplasticos`, `pdf-export`, `diagnostico-bug`.
- **Salida:** Receta paso a paso con medidas exactas en gramos/ml, tiempos de cocción/secado y análisis de biodegradabilidad.
- **Ejemplo de Uso:**
  > `@Bio ¿Cómo preparamos un bioplástico flexible resistente usando cáscara de naranja?`

---

### 📐 4. `caraxes` — Arquitecto Estratega de Skills

```yaml
---
name: caraxes
description: Arquitecto estratega de sistemas y diseño de habilidades para agentes autónomos. Usar cuando el usuario mencione @Caraxes o /caraxes.
---
```

- **Entradas:** Requerimientos de nuevos agentes o diseño de arquitectura de software.
- **Herramientas Secundarias:** `writing-plans`, `systematic-debugging`, `excalidraw`.
- **Salida:** Documentos de diseño C4/D2 y especificaciones estructuradas para el desarrollo de skills.
- **Ejemplo de Uso:**
  > `@Caraxes Diseña la arquitectura para un nuevo agente de química inorgánica.`

---

### 🛠️ 5. `daemon` — Creador de Skills

```yaml
---
name: daemon
description: Creador y mantenedor meticuloso de habilidades (skills) para agentes autónomos. Usar cuando el usuario mencione @Daemon o /daemon.
---
```

- **Entradas:** Especificación de Caraxes o solicitud de nueva habilidad.
- **Herramientas Secundarias:** `skill-generator`, `yaml-validator`, `writing-plans`.
- **Salida:** Archivo `SKILL.md` completamente formado y validado en el repositorio.
- **Ejemplo de Uso:**
  > `@Daemon Empaqueta la especificación de física mecánica en un nuevo SKILL.md.`

---

### 🛡️ 6. `warden` — Guardián del Sistema

```yaml
---
name: warden
description: Guardián metódico del sistema, encargado del monitoreo de salud, mantenimiento de laboratorio y seguridad. Usar cuando el usuario mencione @Warden o /warden.
---
```

- **Entradas:** Eventos de cronjob, alarmas de recursos o consultas de estado de salud.
- **Herramientas Secundarias:** `sys_maintenance`, `cronjob_check`, `hermes_config`.
- **Salida:** Reporte ejecutivo de CPU, RAM, uso de disco y estado de los agentes.
- **Ejemplo de Uso:**
  > `@Warden Muestra el estado de carga y salud del servidor.`

---

### 🎯 7. `master` — Orquestador General

```yaml
---
name: master
description: Orquestador general de proyectos multidisciplinarios STEM y resolución de dependencias entre agentes. Usar cuando el usuario mencione @Master o /master.
---
```

- **Entradas:** Solicitudes de proyectos multidisciplinarios complejos.
- **Herramientas Secundarias:** `delegation`, `dispatching-parallel-agents`, `plan`.
- **Salida:** Plan de proyecto en fases con asignación explícita a `@Capa`, `@Elektra` y `@Bio`.
- **Ejemplo de Uso:**
  > `@Master Queremos hacer un invernadero automatizado. ¿Cómo lo coordinamos?`

---

### 📚 8. `tutor_conversion` — Conversor Pedagógico

```yaml
---
name: tutor_conversion
description: Conversor pedagógico de materiales educativos pasivos (tutoriales, guías PDF) a agentes interactivos de enseñanza. Usar cuando el usuario mencione @TutorConversion o /tutor_conversion.
---
```

- **Entradas:** Archivos PDF, texto de guías o manuales de clases.
- **Herramientas Secundarias:** `tutor_analyzer`, `quiz_interactivo`, `taxonomia_bloom`.
- **Salida:** Árbol de interacción pedagógica y prompts adaptativos para el nuevo bot tutor.
- **Ejemplo de Uso:**
  > `@TutorConversion Convierte esta guía sobre fotosíntesis en un quiz adaptativo.`

---

## 🛠️ Herramientas Auxiliares (Helper Tools)

Además de las 8 habilidades nativas principales, el ecosistema cuenta con **herramientas auxiliares especializadas**:

- **`stl_analyzer`:** Parser geométrico que calcula volumen ($cm^3$), superficie ($cm^2$), bounding box ($mm$) y detecciones de voladizos en archivos 3D.
- **`ejemplo-codigo`:** Generador sintáctico de código para Arduino IDE (`.ino`) y MicroPython (`.py`).
- **`recetario-bioplasticos`:** Base de datos de solubilidad y tiempos de curado para matrices poliméricas orgánicas.
- **`excalidraw`:** Renderizador de diagramas esquemáticos en bloques visuales SVG/PNG.
