# MEMORIA DE INSTINTOS - PROYECTO METROLOGÍA
# Actualizado automáticamente por el Agente tras correcciones del usuario.
# Formato: ID | Confianza (0.3-0.9) | Fuente | Acción

---

## INSTINTOS DE ESTILO (LaTeX / IEEE)

| ID | Instinto | Confianza | Evidencia |
|----|---------|-----------|-----------|
| `latex-usetex-on` | Usar `text.usetex=True` en todos los gráficos de Matplotlib. | 0.9 | Usuario confirmó que MiKTeX está en el PATH (2026-05-16). |
| `autoguardado-3s` | El `autoSaveDelay` debe ser 3000ms, no 1000ms. | 0.8 | Usuario aceptó cambio para evitar compilaciones prematuras (2026-05-16). |

---

## INSTINTOS DE FLUJO DE TRABAJO

| ID | Instinto | Confianza | Evidencia |
|----|---------|-----------|-----------|
| `modelo-latex` | Usar Claude Sonnet para archivos `.tex`. Flash es insuficiente para redacción técnica profunda. | 0.9 | Usuario revirtió a Sonnet para LaTeX tras prueba con Gemini Pro (2026-05-16). |
| `modelo-python` | Usar Gemini Flash para archivos `.py`. Sonnet es excesivo para scripts de graficación. | 0.9 | Preferencia establecida en `settings.json` (2026-05-16). |
| `multimodal-circuitos` | Como Docling omite los textos alternativos, DEBES abrir y analizar visualmente ABSOLUTAMENTE TODAS las imágenes referenciadas en el Markdown (`![...](...png)`). Asume el costo de tokens para no omitir ningún circuito o tabla. | 0.9 | Riesgo (SPOF) aceptado por el usuario: priorizar exactitud sobre costo. |

---

## INSTINTOS PENDIENTES DE CONFIRMACIÓN
> ⚠️ Confianza < 0.7: Aplicar pero consultar al usuario si hay duda.

| ID | Instinto | Confianza | Evidencia |
|----|---------|-----------|-----------|
| `tables-booktabs` | Usar `booktabs` (sin líneas verticales) para tablas de ingeniería. | 0.6 | Estándar IEEE recomendado. Pendiente de corrección del usuario. |

---
> **INSTRUCCIÓN PARA EL AGENTE:** Consulta este archivo antes de comenzar cualquier tarea. Si el usuario hace una corrección que contradiga un instinto existente, actualiza la confianza o elimínalo y añade el nuevo.
