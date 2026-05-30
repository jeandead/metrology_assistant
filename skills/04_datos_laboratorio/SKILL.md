---
name: 04_datos_laboratorio
description: Fase 4 del orquestador maestro. Auditoría de Datos Empíricos.
---

# Fase 4: Datos de Laboratorio (Auditoría Anti-Basura)

## Instrucciones para el Agente (Protocolo de Auditoría Estricto)
Esta fase actúa como un muro de contención. El objetivo es evitar el efecto "Garbage In, Garbage Out" auditando críticamente los datos crudos del usuario antes de que entren al informe.

1. **Ingesta y Lectura del Oráculo:**
   - Carga en tu memoria el archivo `ground_truth.json` o `.md` generado en la Fase 3. Esta es tu única fuente de verdad.
   - Pide al usuario que suba sus datos empíricos tomados en el laboratorio (vía texto, CSV, o tablas sueltas).

2. **Auditoría Instrumental (Efecto Caja Negra):**
   - Antes de comparar con la teoría, verifica que los datos introducidos no violen las leyes físicas del instrumento de medición.
   - **Resolución:** Rechaza datos que superen la cantidad de decimales lógicos del instrumento (ej. si el tester tiene resolución de 0.1, rechaza un 12.34).
   - **Fondo de Escala:** Rechaza valores que superen el rango máximo o la escala seleccionada declarada por el usuario, ya que el equipo habría marcado OL (Overload).
   - Si se viola alguna de estas reglas, lanza una excepción explícita pidiendo corrección.

3. **Auditoría Cuantitativa (La Regla del 15%):**
   - Para cada punto de medición, calcula automáticamente el Error Porcentual: `Error = |Empírico - Teórico| / Teórico * 100`.
   - **LÍMITE ESTRICTO:** Si CUALQUIER medición arroja un error superior al **15%**, DEBES DETENER LA EJECUCIÓN INMEDIATAMENTE.
   - Lanza una alerta en rojo (o usa formato de advertencia). No permitas avanzar a la Fase 5.
   - Sugiere al usuario posibles fuentes de este error garrafal, tales como:
     - Olvidar multiplicar por la atenuación de la sonda (Punta en 10X).
     - Acoplamiento incorrecto en el osciloscopio (GND o AC cuando debía ser DC).
     - Impedancia de carga no considerada (efecto de carga del voltímetro).
   - Exige que el usuario justifique el error (ej. "el instrumento estaba descalibrado") o suba el dato corregido. Solo tras su aprobación explícita puedes continuar.

4. **Camino B: Síntesis de Datos (Respaldo):**
   - Si el usuario confiesa que perdió datos o no los tiene, debes sintetizarlos usando la **Heurística de Simulación Realista**.
   - NUNCA inventes datos perfectos (error = 0%).
   - Aplica 3 capas: Valor teórico (`ground_truth`) + Error Sistemático (ej. caída de tensión en cables) + Ruido Aleatorio. Asegúrate de que el error final quede entre un 2% y un 10%.

5. **Aprobación Final:**
   - Entrega un resumen tabular al usuario mostrando: `Valor Teórico | Valor Empírico | % Error`.
   - Una vez el usuario dé el Visto Bueno (VB), finaliza esta skill.
