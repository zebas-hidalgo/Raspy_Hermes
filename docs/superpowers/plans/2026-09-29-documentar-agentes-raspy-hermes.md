# Documentación Arquitectónica C4 y Flujos de Agentes Hermes en Raspy_Hermes

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Completar la documentación técnica y diagramas arquitectónicos C4 (Container, Sequence Flow y Components en formato Mermaid) para los 7 agentes restantes del ecosistema Raspy_Hermes (Elektra, Bio, Caraxes, Daemon, Warden, Master y Tutor Conversion), siguiendo exactamente la misma lógica y estructura visual que Capa, basados en la configuración y archivos `SOUL.md` extraídos directamente de la Raspberry Pi (10.0.1.15).

**Architecture:** Cada agente dispondrá de su directorio dedicado bajo `docs/<nombre_agente>/` con tres diagramas técnicos en sintaxis Mermaid estricta (`-architecture.mmd`, `-flow.mmd`, `-components.mmd`), además de la actualización de su ficha en `docs/agentes/<nombre_agente>.md` con su identidad, metodología acrónima real (`E.L.E.K.T.R.A.`, `B.I.O.`, `C.A.R.A.X.E.S.`, `D.A.E.M.O.N.`, `W.A.R.D.E.N.`, `M.A.E.S.T.R.O.`, `T.R.A.N.S.F.O.R.M.A.`), marcadores de voz y habilidades activas. Finalmente se sincroniza el README general y se despliegan los cambios a GitHub y a la Raspberry Pi.

**Tech Stack:** Mermaid.js (graph TD, sequenceDiagram, classDiagram/flowchart), Markdown, Git, SSH / Raspberry Pi OS (Hermes Agent Runtime).

---

### Task 1: Elektra / Chispa (Cluster STEM - Electrónica y Microcontroladores)
**Files:**
- Create: `docs/elektra/elektra-architecture.mmd`
- Create: `docs/elektra/elektra-flow.mmd`
- Create: `docs/elektra/elektra-components.mmd`
- Modify: `docs/agentes/elektra.md`

- [ ] **Step 1: Crear diagramas Mermaid de Elektra (Arquitectura, Flujo y Componentes)**
- [ ] **Step 2: Actualizar `docs/agentes/elektra.md` con metodología `E.L.E.K.T.R.A.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Elektra**

---

### Task 2: Bio (Cluster STEM - Bioplásticos y Biomateriales)
**Files:**
- Create: `docs/bio/bio-architecture.mmd`
- Create: `docs/bio/bio-flow.mmd`
- Create: `docs/bio/bio-components.mmd`
- Modify: `docs/agentes/bio.md`

- [ ] **Step 1: Crear diagramas Mermaid de Bio (Arquitectura, Flujo y Componentes con ciclo LCA)**
- [ ] **Step 2: Actualizar `docs/agentes/bio.md` con metodología `B.I.O.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Bio**

---

### Task 3: Caraxes (Cluster Sistema - Arquitectura de Sistemas y Superpowers)
**Files:**
- Create: `docs/caraxes/caraxes-architecture.mmd`
- Create: `docs/caraxes/caraxes-flow.mmd`
- Create: `docs/caraxes/caraxes-components.mmd`
- Modify: `docs/agentes/caraxes.md`

- [ ] **Step 1: Crear diagramas Mermaid de Caraxes (Arquitectura, Flujo y Componentes con Superpowers Framework)**
- [ ] **Step 2: Actualizar `docs/agentes/caraxes.md` con metodología `C.A.R.A.X.E.S.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Caraxes**

---

### Task 4: Daemon / Skill-Creator (Cluster Sistema - Forja de Invocaciones)
**Files:**
- Create: `docs/daemon/daemon-architecture.mmd`
- Create: `docs/daemon/daemon-flow.mmd`
- Create: `docs/daemon/daemon-components.mmd`
- Modify: `docs/agentes/daemon.md`

- [ ] **Step 1: Crear diagramas Mermaid de Daemon (Arquitectura, Flujo y Componentes con forja de skills)**
- [ ] **Step 2: Actualizar `docs/agentes/daemon.md` con metodología `D.A.E.M.O.N.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Daemon**

---

### Task 5: Warden (Cluster Sistema - Guardián y Salud del Sistema)
**Files:**
- Create: `docs/warden/warden-architecture.mmd`
- Create: `docs/warden/warden-flow.mmd`
- Create: `docs/warden/warden-components.mmd`
- Modify: `docs/agentes/warden.md`

- [ ] **Step 1: Crear diagramas Mermaid de Warden (Arquitectura, Flujo y Componentes con monitoreo y mantenimiento)**
- [ ] **Step 2: Actualizar `docs/agentes/warden.md` con metodología `W.A.R.D.E.N.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Warden**

---

### Task 6: Agente Master (Cluster Pedagógico/Orquestación - Director de la Sinfonía de Bots)
**Files:**
- Create: `docs/master/master-architecture.mmd`
- Create: `docs/master/master-flow.mmd`
- Create: `docs/master/master-components.mmd`
- Modify: `docs/agentes/master.md`

- [ ] **Step 1: Crear diagramas Mermaid de Master (Arquitectura C4 multi-agente, Flujo orquestado y Componentes)**
- [ ] **Step 2: Actualizar `docs/agentes/master.md` con metodología `M.A.E.S.T.R.O.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Master**

---

### Task 7: Tutor Conversion (Cluster Pedagógico - Conversor de Agentes)
**Files:**
- Create: `docs/tutor_conversion/tutor_conversion-architecture.mmd`
- Create: `docs/tutor_conversion/tutor_conversion-flow.mmd`
- Create: `docs/tutor_conversion/tutor_conversion-components.mmd`
- Modify: `docs/agentes/tutor_conversion.md`

- [ ] **Step 1: Crear diagramas Mermaid de Tutor Conversion (Arquitectura, Flujo y Componentes con andamiaje pedagógico)**
- [ ] **Step 2: Actualizar `docs/agentes/tutor_conversion.md` con metodología `T.R.A.N.S.F.O.R.M.A.` y links a los diagramas**
- [ ] **Step 3: Validar sintaxis y links de Tutor Conversion**

---

### Task 8: Actualización de README Principal y Sincronización
**Files:**
- Modify: `README.md`
- Sincronizar en Raspberry Pi: `/home/z/Raspy_Hermes`

- [ ] **Step 1: Actualizar matriz y enlaces de arquitectura en README.md**
- [ ] **Step 2: Git commit y push a repositorio remoto GitHub**
- [ ] **Step 3: Ejecutar `git pull` en la Raspberry Pi para sincronizar `/home/z/Raspy_Hermes`**
