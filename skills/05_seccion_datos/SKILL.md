---
name: 05_seccion_datos
description: Fase 5 del orquestador maestro. Redacción Sección de Datos Empíricos.
---

# Fase 5: Redacción Sección de Datos

## Instrucciones para el Agente (Estándar IEEE y LaTeX)
Esta fase toma los datos validados en la Fase 4 y los inyecta en el informe LaTeX (`6resultados_*.tex` o similar) con la máxima calidad tipográfica posible.

1. **Formatos de Tabla Académicos (`booktabs`):**
   - Queda ESTRICTAMENTE PROHIBIDO usar líneas verticales (`|`) o la grilla clásica (`\hline`) para las tablas.
   - DEBES utilizar los comandos del paquete `booktabs`: `\toprule` para el inicio, `\midrule` debajo de los encabezados, y `\bottomrule` al final de la tabla.
   - Aplica el comando `\makecell{... \\ ...}` si un encabezado es muy largo para forzar un salto de línea y evitar el desborde horizontal.

2. **Rigor Numérico (`siunitx` y Cifras Significativas):**
   - Todos los valores numéricos deben presentarse con **exactamente 3 cifras significativas** (salvo que la resolución del instrumento exija más).
   - Usa notación científica estandarizada para valores muy grandes o pequeños (ej. `\num{1.23e-3}`).
   - Elimina la redundancia visual: NO escribas la unidad en cada celda (ej. $12.3 \text{ V}$). La unidad debe ir **exclusivamente** en el encabezado de la columna entre corchetes (ej. `Voltaje [V]`).

3. **Referencias Cruzadas Dinámicas (`\autoref`):**
   - Toda tabla generada debe tener su propio `\label{tab:nombre_descriptivo}` y un `\caption{}` claro.
   - Siempre que redactes un párrafo antes de la tabla para introducirla, DEBES usar `\autoref{tab:nombre_descriptivo}` (ej. "Como se observa en la \autoref{tab:mediciones_trigger}, ..."). No uses "la Tabla 1" en texto duro.

4. **Objetividad de la Sección:**
   - Esta sección es puramente expositiva. Limítate a presentar los datos tabulados ordenadamente.
   - No calcules el error porcentual final aquí, ni redactes conclusiones analíticas (eso pertenece a la Fase 7 de Análisis).
   - Una vez escritas las tablas, pausa y pide validación al usuario.
