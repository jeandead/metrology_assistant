# Contexto de la Conversación: Desarrollo del `metrology-assistant`

Este documento resume el contexto de la conversación previa para que pueda ser retomada en un nuevo chat sin perder información crítica.

## 1. Antecedentes
- **Proyecto original:** Generación, depuración y auditoría de un informe de laboratorio de Metrología Eléctrica (ELI-214) en LaTeX (`C:\Users\Jean\Documents\lab3_2metro`).
- **Problemas resueltos en el proyecto original:** 
  - Corrección de "context rot" (inconsistencias entre el Trabajo Previo teórico y la Metodología práctica).
  - Modificación de archivos LaTeX (`main.tex`, `7analisis.tex`, `9anexo.tex`, `8referencias.tex`) para asegurar cohesión numérica y narrativa.
  - Corrección de errores de compilación por caracteres UTF-8 en scripts de Python (`plot_linearity.py`) inyectados nativamente en el Anexo.
  - Generación de un `cuaderno_laboratorio.md` con los datos empíricos de la Experiencia 03 (Amperímetro analógico).

## 2. Nueva Meta (La Super Skill)
- **Objetivo:** Destilar el flujo de trabajo manual realizado en el proyecto de LaTeX hacia una Skill de nivel Github Developer, pensada para que un tercero (un amigo del usuario) pueda generar informes de metrología fácilmente.
- **Método de diseño:** Se utilizó el comando interactivo `/grill-me` (basado en el marco de la skill `workflow-skill-creator`) para alinear expectativas y resolver ambigüedades arquitectónicas.

## 3. Decisiones Arquitectónicas de la Skill
- **Nombre:** `metrology-assistant`
- **Ubicación futura:** `C:\Users\Jean\.gemini\config\plugins\metrology_project\skills\metrology_report_master\` (o similar) y luego exportado a GitHub.
- **Tipo de Skill:** Orquestador Interactivo (Standard Operating Procedure). No requiere código binario complejo propio, sino que dicta instrucciones precisas de 11 pasos para que el Agente las ejecute interactuando con el usuario por fases.
- **Características clave:**
  - **Eficiencia de Tokens:** Segmentación por fases. El Agente pausa y hace preguntas clave antes de avanzar al siguiente bloque.
  - **El Vault:** Usa `list_dir` y `view_file` en la ruta relativa `resources/MetrologiaVault/` dentro del repositorio de la skill para encontrar apuntes teóricos de manera portable.
  - **Simulación de datos:** Si el usuario no tiene datos de laboratorio, la skill instruye sintetizar valores con tolerancia empírica, presentarlos como reales y generar un `cuadernillo_laboratorio.md` para el usuario.
  - **Scripts de Análisis:** El agente programa scripts en Python, los guarda en la carpeta `<proyecto_latex>/scripts/` y los ejecuta autónomamente usando comandos de terminal (`run_command`) para compilar los gráficos finales para el LaTeX.
  - **Prevención de Context-Rot:** Al final de la redacción, el agente orquestador invoca subagentes paralelos (`invoke_subagent`) para auditar la coherencia entre Resultados, Conclusiones y Resumen Ejecutivo.

## 4. Estado Actual y Próximos Pasos
- El diseño detallado y definitivo de esta arquitectura fue exportado exitosamente al archivo `implementation_plan.md` en esta misma carpeta (`C:\Users\Jean\Documents\metrology_assistant`).
- **Paso inmediato a seguir en el nuevo chat:** Leer este `context.md` y el `implementation_plan.md`, y proceder inmediatamente con la **fase de implementación**: programar la Skill, crear su directorio en la carpeta de plugins locales del usuario y escribir el `SKILL.md` maestro junto con sus plantillas base.
