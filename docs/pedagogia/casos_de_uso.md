[← Volver al README Principal](../../README.md) • [🍎 Guía Docentes](guias_docentes.md) • [🚀 Manual Estudiantes](guia_interaccion_estudiantes.md)

---

# 💡 Casos de Uso Reales Multidisciplinarios

Este documento muestra cómo interactúan los agentes de **Raspy_Hermes** para resolver proyectos escolares reales en **Kronos_School**.

---

## 🌻 Caso 1: Maceta Eco-Inteligente Autorregable

### 🎯 Objetivo del Proyecto:
Construir una maceta fabricada con bioplástico reciclable, equipada con un sensor de humedad de suelo y una bomba de agua controlada por Arduino.

```
       [ @Master ] Organiza el proyecto
           │
           ├─► [ @Bio ] Formula la masa bioplástica para la maceta
           ├─► [ @Capa ] Diseña el soporte 3D y molde cero residuos
           └─► [ @Elektra ] Programa el sensor de humedad y bomba 5V
```

### 💬 Flujo de Interacción en la Plataforma:

1. **Estudiante:** `@Master Queremos hacer una maceta que se riegue sola usando bioplástico. ¿Cómo nos organizamos?`
2. **@Master:** *"¡Excelente proyecto! Dividamos el trabajo:*
   - *@Bio diseñará la mezcla de almidón y glicerina para el cuerpo de la maceta.*
   - *@Capa modelará el soporte impermeable 3D para alojar la electrónica.*
   - *@Elektra programará el sensor de humedad en Arduino.*"
3. **Estudiante:** `@Bio ¿Qué proporciones necesitamos para que la maceta sea resistente al agua pero biodegradable?`
4. **@Bio:** *"Usa 20g de almidón de maíz, 5ml de glicerina, 3ml de vinagre blanco y 100ml de agua. Hornea a 60°C por 2 horas para maximizar la rigidez."*
5. **Estudiante:** `@Elektra ¿Cómo conectamos el sensor de humedad FC-28 a la placa Arduino?`
6. **@Elektra:** *"Conecta VCC a 5V, GND a Tierra y A0 al pin analógico A0. Aquí tienes el código `.ino` para activar el relé cuando la humedad sea menor al 30%..."*

---

## 🦾 Caso 2: Mini Brazo Robótico Educativo

### 🎯 Objetivo del Proyecto:
Imprimir las piezas mecánicas de un brazo de 3 ejes y controlar servomotores SG90 mediante un potenciómetro.

### 💬 Flujo de Interacción:

1. **@Capa:** Analiza los archivos STL del brazo robótico y sugiere una densidad de relleno giroide del 20% para equilibrar resistencia y bajo peso (evitando sobrecargar los servos).
2. **@Elektra:** Proporciona el esquema de conexiones para alimentar los 3 servomotores con una fuente externa de 5V (resguardando el Arduino) y entrega el sketch con la librería `<Servo.h>`.
3. **@Warden:** Monitorea la sesión para garantizar que el número de comandos procesados se mantenga dentro del límite seguro.

---

## 📚 Caso 3: Transformación de Guía en Bot Tutor

### 🎯 Objetivo del Proyecto:
Convertir un PDF estático sobre *"El Ciclo del Agua y la Evaporación"* en un bot tutor interactivo para estudiantes.

### 💬 Flujo de Interacción:

1. **Docente:** `@TutorConversion Adjunto la guía en PDF. Queremos convertirla en un bot de preguntas adaptativas.`
2. **@TutorConversion:** Extrae los conceptos clave (Evaporación, Condensación, Precipitación), los categoriza según la Taxonomía de Bloom y genera un árbol de diálogo.
3. **@Daemon:** Toma la especificación de `@TutorConversion` y empaqueta la nueva habilidad `ciclo_agua_tutor/SKILL.md` dentro del catálogo de Hermes Agent.

---

[← Volver al README Principal](../../README.md)
