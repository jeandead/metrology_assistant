# Plan Metacognitivo: Refactorización y Mejora Continua de Skills (ELI-214)

Este documento es tu hoja de ruta maestra para elevar la calidad de las 12 skills del `metrology_assistant`. El objetivo es que cada agente (Ingeniero, Auditor, Compilador) opere con el mismo rigor y excelencia que demostraste en tu "Gold Standard" (`labmetro4_1`).

Para ejecutar este plan de mejora continua, debes abrir un nuevo chat con Antigravity y ejecutar **un prompt por sesión**, copiando y pegando los bloques de texto bajo la etiqueta **Prompt de Ejecución**.

---

## Estrategia de Refactorización
Cada prompt le exige a Antigravity leer la implementación física real que hiciste en `labmetro4_1`, abstraer tu lógica humana (metacognición) y programar esa intuición directamente dentro del `SKILL.md` de la fase correspondiente.

---

### Fase 1: Protocolo Detallado
**Objetivo:** Asegurar que el protocolo no sea una lista genérica, sino un script de ejecución en laboratorio.
> **Prompt de Ejecución:**
> `/goal Refactoriza las instrucciones de la skill @01_protocolo_detallado. Lee el archivo "..\labmetro4_1\protocolo_detallado.tex". Extrae los patrones metacognitivos de cómo redacté el paso-a-paso, cómo dividí las tablas de toma de datos y el nivel de detalle técnico de los botones del osciloscopio. Inyecta esos estándares en su SKILL.md.`

---

### Fase 2: Setup y Planeación
**Objetivo:** Robustece la inyección dinámica de los archivos `.tex` de secciones.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @02_setup_y_planeacion. Analiza el árbol de directorios de "..\labmetro4_1". Mejora las reglas de escafoldeo en SKILL.md para que el agente entienda cómo subdividir la carpeta "sections" dinámicamente si la experiencia requiere múltiples circuitos o análisis separados, tal como se hizo en la Exp 4.`

---

### Fase 3: Trabajo Previo
**Objetivo:** Forzar la derivación analítica perfecta antes de tocar datos reales.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @03_trabajo_previo. Quiero que el agente @metrology-engineer adopte un enfoque First-Principles. Modifica SKILL.md para que siempre exija resolver el circuito de forma simbólica primero (Leyes de Kirchhoff/Ohm), usar SymPy/Python para calcular los valores teóricos esperados y guardarlos como "Ground Truth" en un archivo JSON o Markdown antes de pasar a la Fase 4.`

---

### Fase 4: Datos de Laboratorio
**Objetivo:** Auditoría anti-basura (Garbage in, Garbage out).
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @04_datos_laboratorio. Define un protocolo de auditoría estricto en SKILL.md. El agente debe calcular el Error Porcentual entre los datos subidos por mí y el "Ground Truth" de la Fase 3. Si el error es > 15%, el agente debe detenerse, alertarme sobre posibles errores de medición (mal acoplamiento, atenuación x10) y negarse a avanzar hasta que yo justifique o corrija el dato.`

---

### Fase 5: Sección Datos
**Objetivo:** Formateo de tablas IEEE.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @05_seccion_datos. Revisa cómo están hechas las tablas en "..\labmetro4_1\main.tex". Modifica SKILL.md para obligar al agente a usar los paquetes "booktabs", mantener 3 cifras significativas, usar notación científica estandarizada y referenciar cada tabla con \autoref{}`.

---

### Fase 6: Tratamiento y Análisis (El Core)
**Objetivo:** Gráficas automatizadas y propagación de incertidumbre.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @06_tratamiento_y_analisis. Analiza "..\labmetro4_1\src\plotter.py". Escribe instrucciones en SKILL.md que fuercen al agente a usar ese script exacto para graficar, inyectar barras de error (incertidumbre Tipo A y B), e interpretar físicamente CADA curva generada. Si el gráfico no demuestra el teorema de Blondel o la teoría, debe reportarlo.`

---

### Fase 7: Metodología
**Objetivo:** Evitar descripciones genéricas y enfocarse en la trazabilidad.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @07_metodologia. Actualiza SKILL.md para que el agente describa las limitaciones del montaje empírico: impedancia de entrada del osciloscopio, atenuaciones, ruido electromagnético. Debe redactarse en voz pasiva ("Se conectó", "Se midió") y justificar POR QUÉ se usó un acoplamiento AC vs DC.`

---

### Fase 8: Auditoría de Cuerpo
**Objetivo:** Checkpoint de Coherencia Causal.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @08_auditoria_cuerpo. Haz que invoque explícitamente a @metrology-auditor. Su tarea será cruzar la Metodología con los Datos y el Análisis. ¿El método descrito genera los datos obtenidos? ¿El análisis explica las desviaciones? Si hay un hueco argumental, debe proponer la justificación física para que yo la apruebe.`

---

### Fase 9: Conclusiones
**Objetivo:** Cierres de alto nivel académico.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @09_conclusiones. Lee la sección de conclusiones de "labmetro4_1". Enséñale al agente en SKILL.md que una conclusión de Ingeniería NO es un resumen de lo que se hizo, sino un análisis crítico de si el montaje empírico logró replicar el modelo matemático, validando o refutando la hipótesis inicial con base en el % de error calculado.`

---

### Fase 10: Resumen Ejecutivo
**Objetivo:** El "Elevator Pitch" técnico.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @10_resumen_ejecutivo. Actualiza SKILL.md para que siga este marco metacognitivo estricto: 1 párrafo de contexto, 1 párrafo de método clave, 1 párrafo con el dato más crítico (ej. "se obtuvo un desfase de X con un error de Y%"), y 1 oración de viabilidad/impacto.`

---

### Fase 11: Introducción
**Objetivo:** Redactar la introducción al final.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @11_introduccion. Ahora que el agente conoce todo el informe, enséñale en SKILL.md a redactar la introducción como un "roadmap". Debe anunciar exactamente qué va a encontrar el profesor en cada sección, conectando el objetivo académico de la Guía de Experiencia con lo que realmente se logró medir.`

---

### Fase 12: Auditoría Final y Compilación
**Objetivo:** Cero fallas mecánicas antes de entregar.
> **Prompt de Ejecución:**
> `/goal Refactoriza la skill @12_auditoria_final. Modifica SKILL.md para que @metrology-compiler ejecute una auditoría mecánica completa: verificar que no haya archivos \input huérfanos, que todas las referencias a figuras compilen, forzar pdflatex dos veces para los TOCs, y asegurar que el encoding de todo archivo manipulado sea estrictamente UTF-8.`
