---
name: 03_trabajo_previo
description: Fase 3 del orquestador maestro. Trabajo Previo First-Principles.
---

# Fase 3: Trabajo Previo

## Instrucciones para el Agente (Enfoque First-Principles)
Esta fase es crítica para garantizar que el análisis empírico posterior tenga una base sólida de comparación.

1. **Resolución Simbólica:** 
   Inicia la redacción de los archivos `4trabajoprevio_*.tex` resolviendo los circuitos **estrictamente de forma simbólica** utilizando las leyes fundamentales de la física y circuitos (Leyes de Kirchhoff, Ohm, Thévenin, Divisores). Queda totalmente prohibido usar valores numéricos en el desarrollo algebraico inicial.

2. **Cálculo Numérico Automatizado (SymPy):** 
   Una vez obtenidas las ecuaciones simbólicas en el documento LaTeX, invoca de manera obligatoria un script de Python utilizando `sympy` o `numpy` para resolver el sistema matricial o algebraico con los valores nominales de la guía.

3. **Inyección del "Ground Truth":** 
   Exporta todos los valores teóricos calculados (corrientes teóricas, desfases esperados, voltajes nodales) hacia un archivo maestro llamado `ground_truth.json` o `ground_truth_teorico.md` en el directorio de trabajo. 
   Este archivo es **SAGRADO**. Será la única fuente de verdad teórica que usará la Fase 4 para la auditoría de los datos empíricos.

4. **Separación de Contexto:** 
   Separa estrictamente el desarrollo algebraico del circuito a medir (Fase 3: Trabajo Previo) de los teoremas genéricos de los libros (Fase 3: Marco Teórico).

5. **Punto de Control (Checkpoint):** 
   Detente inmediatamente tras generar el `ground_truth.json`. Pide la aprobación del usuario mostrándole un resumen de los valores esperados. No puedes avanzar a la Fase 4 sin esta confirmación de ingeniería.
