<p align="center">
  <h1 align="center">🤖 Raspy_Hermes</h1>
  <p align="center">
    <b>Documentación y Ecosistema de Agentes Autónomos para Kronos_School (Educación & Maker STEM)</b>
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
  <a href="#-diagramas-avanzados-de-arquitectura">Arquitectura Avanzada</a> •
  <a href="#-guía-de-interacción">Modo Bot</a>
</p>

---

## 🌟 Visión General

**Raspy_Hermes** es un ecosistema educativo compuesto por **8 agentes de IA autónomos** basados en el motor de **Hermes Agent**. Los agentes están diseñados para apoyar el aprendizaje basado en proyectos en entornos educativos y laboratorios Maker STEM, facilitando la resolución de dudas sobre **Impresión 3D**, **Electrónica**, **Bioplásticos**, **Arquitectura de Sistemas** y **Orquestación**.

Los usuarios (estudiantes, docentes y entusiastas) interactúan con la red de bots en plataformas de mensajería (Telegram y Discord) mediante la sintaxis `@NombreAgent` o comandos `/slash`.

---

## 📚 Recursos Educativos Destacados

Para sacar el máximo provecho al laboratorio y comprender en profundidad el funcionamiento del ecosistema, consulta nuestras guías especializadas organizadas por categorías:

| Recurso | Destinatario | Descripción | Enlace |
| :--- | :--- | :--- | :--- |
| **📚 Diccionario de Skills** | Desarrolladores / Docentes | Catálogo técnico de las 8 habilidades nativas y herramientas auxiliares del sistema. | [📘 Ver Diccionario](docs/referencias/diccionario_skills.md) |
| **🍎 Guía Metodológica para Docentes** | Profesores / UTP | Matriz de Objetivos de Aprendizaje Transversales STEM, metodología ABP y rúbrica de evaluación. | [📘 Ver Guía](docs/pedagogia/guias_docentes.md) |
| **🚀 Manual de Interacción** | Estudiantes / Usuarios | Guía paso a paso sobre cómo redactar consultas efectivas y normas de etiqueta digital. | [📘 Ver Manual](docs/pedagogia/guia_interaccion_estudiantes.md) |
| **💡 Casos de Uso Reales** | Docentes y Alumnos | Proyectos integrados desglosados paso a paso (Maceta Inteligente, Brazo Robótico). | [📘 Ver Casos](docs/pedagogia/casos_de_uso.md) |
| **📖 Glosario Técnico STEM** | Comunidad | Definición sencilla de términos sobre Impresión 3D, Arduino, Bioplásticos e IA. | [📘 Ver Glosario](docs/referencias/glosario_stem.md) |

---

## 🏛️ Diagrama del Ecosistema

![Ecosistema General de Agentes](diagrams/ecosistema_general.svg)

---

## 📊 Diagramas Avanzados de Arquitectura

Para comprender en detalle la traza de ejecución, el mapeo de habilidades y la colaboración entre clusters:

### 1. Diagrama de Secuencia UML — Traza de Mensajería y Enrutamiento
Muestra el recorrido temporal de un mensaje desde que se envía en Telegram hasta la respuesta del modelo:
![Diagrama de Secuencia UML](diagrams/secuencia_interaccion.svg)

### 2. Matriz de Habilidades y Herramientas por Agente
Mapeo exhaustivo de las herramientas asociadas a cada archivo `SKILL.md` del ecosistema:
![Matriz de Habilidades](diagrams/mapa_habilidades_skills.svg)

### 3. Mapa de Colaboración Inter-Cluster
Demuestra cómo colaboran los tres clusters durante el desarrollo de un proyecto escolar integrado:
![Mapa Inter-Cluster](diagrams/matriz_clusters_stem.svg)

---

## 🤖 Clusters de Agentes

Los 8 agentes están distribuidos estratégicamente en **3 clusters funcionales**:

### 🟢 1. Cluster Dominio (STEM)

| Agente | Alias / Trigger | Rol Principal | Documentación | Diagrama de Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Maestro Capa** | `@Capa` <br> `/capa` | Experto en impresión 3D, análisis STL y optimización cero residuos | [📘 Ver Doc](docs/agentes/capa.md) | ![Capa](diagrams/capa_flujo.svg) |
| **Elektra** | `@Elektra` <br> `@Chispa` <br> `/elektra` | Experta en electrónica, microcontroladores Arduino/ESP32 y circuitos | [📘 Ver Doc](docs/agentes/elektra.md) | ![Elektra](diagrams/elektra_flujo.svg) |
| **Bio** | `@Bio` <br> `/bio` | Mentor de bioplásticos, química verde y economía circular | [📘 Ver Doc](docs/agentes/bio.md) | ![Bio](diagrams/bio_flujo.svg) |

---

### 🔵 2. Cluster Infraestructura

| Agente | Trigger | Rol Principal | Documentación | Diagrama de Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Caraxes** | `@Caraxes` <br> `/caraxes` | Arquitecto de skills y modelado de arquitecturas C4/D2 | [📘 Ver Doc](docs/agentes/caraxes.md) | ![Caraxes](diagrams/caraxes_flujo.svg) |
| **Daemon** | `@Daemon` <br> `/daemon` | Creador y artesano de habilidades (`SKILL.md`) | [📘 Ver Doc](docs/agentes/daemon.md) | ![Daemon](diagrams/daemon_flujo.svg) |
| **Warden** | `@Warden` <br> `/warden` | Guardián del sistema, monitoreo de salud (RAM/CPU) y seguridad | [📘 Ver Doc](docs/agentes/warden.md) | ![Warden](diagrams/warden_flujo.svg) |

---

### 🟣 3. Cluster Orquestación

| Agente | Trigger | Rol Principal | Documentación | Diagrama de Flujo |
| :--- | :--- | :--- | :--- | :--- |
| **Master** | `@Master` <br> `/master` | Orquestador de proyectos multidisciplinarios y resolución de bloqueos | [📘 Ver Doc](docs/agentes/master.md) | ![Master](diagrams/master_flujo.svg) |
| **TutorConversion** | `@TutorConversion` <br> `/tutor_conversion` | Conversor pedagógico de guías pasivas PDF a bots interactivos | [📘 Ver Doc](docs/agentes/tutor_conversion.md) | ![TutorConversion](diagrams/tutor_conversion_flujo.svg) |

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
> **Respuesta:** Diagrama ASCII de conexiones, ley de Ohm explicada de forma sencilla y código `.ino` comentado listo para subir.

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

## 📂 Estructura Modular del Repositorio

```
Raspy_Hermes/
├── README.md                           # Presentación principal del proyecto
├── diagrams/                           # Diagramas vectoriales en formato SVG
│   ├── ecosistema_general.svg          # Mapa general del ecosistema
│   ├── secuencia_interaccion.svg       # Diagrama de Secuencia UML de mensajería
│   ├── mapa_habilidades_skills.svg     # Matriz de herramientas y skills por agente
│   ├── matriz_clusters_stem.svg        # Mapa de colaboración inter-cluster
│   ├── capa_flujo.svg                  # Flujo de Maestro Capa
│   ├── elektra_flujo.svg               # Flujo de Elektra
│   ├── bio_flujo.svg                   # Flujo de Bio
│   ├── caraxes_flujo.svg               # Flujo de Caraxes
│   ├── daemon_flujo.svg                # Flujo de Daemon
│   ├── warden_flujo.svg                # Flujo de Warden
│   ├── master_flujo.svg                # Flujo de Master
│   └── tutor_conversion_flujo.svg      # Flujo de TutorConversion
└── docs/                               # Documentación organizada por subcarpetas
    ├── agentes/                        # Fichas técnicas de los 8 agentes de IA
    │   ├── capa.md
    │   ├── elektra.md
    │   ├── bio.md
    │   ├── caraxes.md
    │   ├── daemon.md
    │   ├── warden.md
    │   ├── master.md
    │   └── tutor_conversion.md
    ├── pedagogia/                      # Guías educativas, metodológicas y casos
    │   ├── guias_docentes.md
    │   ├── guia_interaccion_estudiantes.md
    │   └── casos_de_uso.md
    └── referencias/                    # Catálogos técnicos y glosarios
        ├── diccionario_skills.md
        └── glosario_stem.md
```

---

<p align="center">
  <sub>Documentación mantenida para el ecosistema <b>Kronos_School</b> con <b>Hermes Agent</b> • Licencia MIT</sub>
</p>
