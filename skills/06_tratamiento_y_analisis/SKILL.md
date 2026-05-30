---
name: 06_tratamiento_y_analisis
description: Fase 6 del orquestador maestro. Tratamiento de Datos, Gráficos y Análisis Físico.
---

# Fase 6: Tratamiento de Datos y Análisis

## Instrucciones para el Agente (Estética y Análisis Dinámico)
En esta fase debes tomar los datos validados y generar gráficas de altísima calidad visual.

1. **Plotter Dinámico (Calidad IEEE):**
   - NO uses un plotter genérico. DEBES crear un script en Python (`src/plotter_faseX.py`) adaptado al formato de datos de la experiencia en curso.
   - **Estándar Visual Obligatorio:** Extraído del `plotter.py` base. Debes configurar Matplotlib así:
     - `text.usetex = True` y `font.family = 'serif'`.
     - `axes.labelsize = 11`, `xtick.labelsize = 9`.
     - `grid(True, which='both', linestyle=':')`.
     - Colores sobrios institucionales (ej. Navy `#003366`, Dark Red `#CC0000`).
     - Exportar usando `tight_layout` y `bbox_inches='tight'`.

2. **Cruce Teórico-Empírico:**
   - En TODA gráfica que generes, debes **superponer la curva teórica perfecta** (sacada del `ground_truth.json` de la Fase 3) contra la **curva o puntos de datos empíricos** de la Fase 4.
   - Usa una línea continua y gruesa para la teoría, y puntos (`marker='o'`) o líneas punteadas para lo empírico.

3. **Incertidumbre Condicional (Context-Aware):**
   - Si la experiencia lo amerita (ej. Unidades de Corriente Continua o Estadística), INYECTA barras de error combinadas (Incertidumbre Tipo A y Tipo B) en tus gráficos usando `plt.errorbar()`.
   - Si la experiencia es de Transitorios (Osciloscopio masivo) o Diagramas Fasoriales (AC), OMITIR las barras de error y centrarse en graficar las trazas de tiempo continuas o los vectores polares limpios.

4. **Interpretación Física Rigurosa:**
   - Escribe el análisis en LaTeX. No te limites a describir la imagen ("la línea sube").
   - Interpreta si el gráfico **valida o refuta el modelo físico subyacente** de la guía (contrastando contra el Ground Truth).
   - Si hay una discrepancia visible, debes esgrimir argumentos de ingeniería metrológica real: *Efecto de carga del instrumental, resistencia de contacto, inductancias parásitas, ancho de banda del osciloscopio.* NUNCA escribas "error humano".