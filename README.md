<p align="center">
  <h1 align="center">🤖 Raspy_Hermes</h1>
  <p align="center">
    <b>Documentación y Ecosistema de Agentes Autónomos para Kronos_School (6to Grado STEM)</b>
  </p>
</p>

<p align="center">
  <img alt="Licencia MIT" src="https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge&logo=opensourceinitiative&logoColor=white">
  <img alt="Entorno Kronos_School" src="https://img.shields.io/badge/Entorno-Kronos__School-emerald.svg?style=for-the-badge&logo=education&logoColor=white">
  <img alt="Agentes" src="https://img.shields.io/badge/Agentes-8%20Bots-7c3aed.svg?style=for-the-badge&logo=probot&logoColor=white">
  <img alt="Último Commit" src="https://img.shields.io/github/last-commit/zebas-hidalgo/Raspy_Hermes?style=for-the-badge&color=0284c7&logo=git&logoColor=white">
  <img alt="Formato Diagramas" src="https://img.shields.io/badge/Diagramas-SVG%20Vectorial-f59e0b.svg?style=for-the-badge&logo=svg&logoColor=white">
</p>

<p align="center">
  <a href="#-visión-general">Visión General</a> •
  <a href="#-recursos-educativos-destacados">Recursos Educativos</a> •
  <a href="#-clusters-de-agentes">Clusters</a> •
  <a href="#-diagrama-del-ecosistema">Arquitectura</a> •
  <a href="#-guía-de-interacción">Modo Bot</a>
</p>

---

## 🌟 Visión General

**Raspy_Hermes** es un ecosistema educativo compuesto por **8 agentes de IA autónomos** basados en el motor de **Hermes Agent**. Los agentes están diseñados para apoyar el aprendizaje basado en proyectos STEM en 6to grado básico (Chile), facilitando la resolución de dudas sobre **Impresión 3D**, **Electrónica**, **Bioplásticos**, **Arquitectura de Sistemas** y **Orquestación**.

Los usuarios (estudiantes y profesores) interactúan con la red de bots en plataformas de mensajería (Telegram y Discord) mediante la sintaxis `@NombreAgent` o comandos `/slash`.

---

## 📚 Recursos Educativos Destacados

Para sacar el máximo provecho al laboratorio y comprender en profundidad el funcionamiento del ecosistema, consulta nuestras guías especializadas:

| Recurso | Destinatario | Descripción | Enlace |
| :--- | :--- | :--- | :--- |
| **🍎 Guía Metodológica para Docentes** | Profesores / UT P | Matriz de Objetivos de Aprendizaje (Mineduc Chile), metodología ABP y rúbrica de evaluación. | [📘 Ver Guía](docs/GUIAS_DOCENTES.md) |
| **🚀 Manual de Interacción** | Estudiantes | Guía paso a paso sobre cómo redactar consultas efectivas y normas de etiqueta digital. | [📘 Ver Manual](docs/GUIA_INTERACCION.md) |
| **💡 Casos de Uso Reales** | Docentes y Alumnos | Proyectos integrados desglosados paso a paso (Maceta Inteligente, Brazo Robótico). | [📘 Ver Casos](docs/CASOS_DE_USO.md) |
| **📖 Glosario Técnico STEM** | Comunidad | Definición sencilla de términos sobre Impresión 3D, Arduino, Bioplásticos e IA. | [📘 Ver Glosario](docs/GLOSARIO.md) |

---

## 🏛️ Diagrama del Ecosistema

![Ecosistema General de Agentes](diagrams/ecosistema_general.svg)

---

## 🤖 Clusters de Agentes

Los 8 agentes están distribuidos estratégicamente en **3 clusters funcionales**:

### 🟢 1. Cluster Dominio (STEM)

| Agente | Alias / Trigger | Rol Principal | Documentación | Diagrama de Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Maestro Capa** | `@Capa` <br> `/capa` | Experto en impresión 3D, análisis STL y optimización cero residuos | [📘 Ver Doc](docs/capa.md) | ![Capa](diagrams/capa_flujo.svg) |
| **Elektra** | `@Elektra` <br> `@Chispa` <br> `/elektra` | Experta en electrónica, microcontroladores Arduino/ESP32 y circuitos | [📘 Ver Doc](docs/elektra.md) | ![Elektra](diagrams/elektra_flujo.svg) |
| **Bio** | `@Bio` <br> `/bio` | Mentor de bioplásticos, química verde y economía circular | [📘 Ver Doc](docs/bio.md) | ![Bio](diagrams/bio_flujo.svg) |

---

### 🔵 2. Cluster Infraestructura

| Agente | Trigger | Rol Principal | Documentación | Diagrama de Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Caraxes** | `@Caraxes` <br> `/caraxes` | Arquitecto de skills y modelado de arquitecturas C4/D2 | [📘 Ver Doc](docs/caraxes.md) | ![Caraxes](diagrams/caraxes_flujo.svg) |
| **Daemon** | `@Daemon` <br> `/daemon` | Creador y artesano de habilidades (`SKILL.md`) | [📘 Ver Doc](docs/daemon.md) | ![Daemon](diagrams/daemon_flujo.svg) |
| **Warden** | `@Warden` <br> `/warden` | Guardián del sistema, monitoreo de salud (RAM/CPU) y seguridad | [📘 Ver Doc](docs/warden.md) | ![Warden](diagrams/warden_flujo.svg) |

---

### 🟣 3. Cluster Orquestación

| Agente | Trigger | Rol Principal | Documentación | Diagrama de Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Master** | `@Master` <br> `/master` | Orquestador de proyectos multidisciplinarios y resolución de bloqueos | [📘 Ver Doc](docs/master.md) | ![Master](diagrams/master_flujo.svg) |
| **TutorConversion** | `@TutorConversion` <br> `/tutor_conversion` | Conversor pedagógico de guías pasivas PDF a bots interactivos | [📘 Ver Doc](docs/tutor_conversion.md) | ![TutorConversion](diagrams/tutor_conversion_flujo.svg) |

---

## 💬 Guía de Interacción en Modo Bot

<details>
<summary>👉 <b>Haz clic aquí para ver ejemplos de preguntas y comandos en Telegram/Discord</b></summary>

<br>

#### 🖨️ Mención a @Capa:
```text
@Capa ¿Cuál es la temperatura óptima para imprimir PLA en una Ender 3?
```
> **Respuesta:** Parámetros exactos (Extrusor: 205°C, Cama: 55°C, Velocidad: 50mm/s), análisis de adherencia y tips de cero residuos.

#### ⚡ Mención a @Elektra:
```text
@Elektra ¿Cómo conecto una fotoresistencia LDR a un Arduino para encender un LED?
```
> **Respuesta:** Diagrama ASCII de conexiones, ley de Ohm explicada para 11 años y código `.ino` comentado listo para subir.

#### 🌿 Mención a @Bio:
```text
@Bio ¿Cómo podemos hacer bioplástico flexible con almidón de maíz en el laboratorio?
```
> **Respuesta:** Receta con proporciones exactas en gramos/ml, tiempos de secado y estimación de biodegradación.

#### 🎯 Mención a @Master:
```text
@Master Queremos diseñar una estación meteorológica escolar con carcasa 3D y sensores solares. ¿Cómo nos organizamos?
```
> **Respuesta:** Desglose del proyecto en 3 fases asignando tareas específicas a `@Capa`, `@Elektra` y `@Bio`.

</details>

---

## 📂 Estructura del Repositorio

```
Raspy_Hermes/
├── README.md                           # Presentación principal del proyecto
├── diagrams/                           # Diagramas vectoriales en formato SVG
│   ├── ecosistema_general.svg
│   ├── capa_flujo.svg
│   ├── elektra_flujo.svg
│   ├── bio_flujo.svg
│   ├── caraxes_flujo.svg
│   ├── daemon_flujo.svg
│   ├── warden_flujo.svg
│   ├── master_flujo.svg
│   └── tutor_conversion_flujo.svg
└── docs/                               # Documentación pedagógica y por agente
    ├── GUIAS_DOCENTES.md               # Guía metodológica para profesores y rúbrica
    ├── GUIA_INTERACCION.md             # Manual para estudiantes e ingeniería de prompts
    ├── CASOS_DE_USO.md                 # Ejemplos de proyectos reales multidisciplinarios
    ├── GLOSARIO.md                     # Glosario técnico de términos STEM
    ├── capa.md
    ├── elektra.md
    ├── bio.md
    ├── caraxes.md
    ├── daemon.md
    ├── warden.md
    ├── master.md
    └── tutor_conversion.md
```

---

<p align="center">
  <sub>Documentación mantenida para el ecosistema <b>Kronos_School</b> con <b>Hermes Agent</b> • Licencia MIT</sub>
</p>
