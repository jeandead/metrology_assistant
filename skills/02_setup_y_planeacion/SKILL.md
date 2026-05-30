---
name: 02_setup_y_planeacion
description: Fase 2 del orquestador maestro. Escafoldear proyecto e inyectar templates.
---

# Fase 2: Setup y Planeación

## Instrucciones para el Agente
Esta skill es invocada para crear la estructura de un nuevo informe de laboratorio desde cero, utilizando los templates base destilados de `labmetro4_1`.

1. **Creación de Estructura de Directorios:**
   Genera estricta y obligatoriamente el siguiente árbol de directorios en el directorio de trabajo (donde el usuario invocó la tarea):
   ```text
   ├───.antigravity
   ├───Recursos
   ├───requisitos
   ├───sections
   └───src
       └───imagenes
   ```

2. **Copia de Templates Globales (Vía Plugin Path):**
   Debes leer los archivos ubicados en el directorio de templates de este plugin y escribirlos hacia el directorio actual de trabajo del usuario (Workspace):
   - Leer `templates/main.tex` del plugin -> Escribir en `main.tex` del usuario
   - Leer `templates/guia_de_estilo.md` del plugin -> Escribir en `guia_de_estilo.md` del usuario
   - Leer `templates/plotter.py` del plugin -> Escribir en `src/plotter.py` del usuario
   - Leer `templates/rules.md` del plugin -> Escribir en `.antigravity/rules.md` del usuario
   - Leer `templates/instintos.md` del plugin -> Escribir en `.antigravity/instintos.md` del usuario

3. **Inyección de Identidad:**
   Edita `main.tex` para rellenar los placeholders: `[NUMERO]`, `[TITULO DE LA EXPERIENCIA]`, `[GRUPO]`, `[NOMBRE AUTOR X]`, etc. Pregunta al usuario por estos datos si no los conoces.

4. **Escafoldeo de Secciones Híbrido (.tex):**
   - **Arquitectura Base (9 Pilares):** Todo informe debe contener, como mínimo, la siguiente estructura maestra:
     1. `1resumen_ejecutivo.tex`
     2. `2introduccion.tex`
     3. `3marcoteorico.tex`
     4. `4trabajoprevio_main.tex`
     5. `5metodologia_main.tex`
     6. `6resultados_main.tex`
     7. `7analisis_main.tex`
     8. `8conclusiones.tex`
     9. `9referencias.tex`
     10. `10anexos.tex`
   - **Subdivisión Atómica por Circuito (Opción B):** Si la Guía de Experiencia contiene múltiples experimentos o circuitos (ej. "A", "B", "C"), DEBES subdividir los pilares Core (4, 5, 6 y 7).
     - Por ejemplo, en lugar de poner todo el texto en `5metodologia_main.tex`, crea `5metodologia_A.tex` y `5metodologia_B.tex`.
   - **LaTeX Limpio (`_main.tex`):** Para mantener la limpieza del `main.tex` global, las declaraciones de título (ej. `\section{Metodología Experimental}`) deben ir DENTRO de los archivos `_main.tex` (ej. `5metodologia_main.tex`). Luego, ese mismo archivo `_main.tex` será el encargado de hacer `\input{sections/5metodologia_A}` y `\input{sections/5metodologia_B}`.
   - El archivo `main.tex` global del directorio raíz solo hará `\input{sections/5metodologia_main}`.

5. **Validación:**
   - Comprueba que la estructura `tree /F` coincide con lo esperado.
   - Pide permiso al usuario para compilar por primera vez y verificar que el PDF compila limpiamente.
