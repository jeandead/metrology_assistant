# Master Plan: Plugin `metrology-assistant` (ELI-214)

Gracias a tus respuestas, la arquitectura ahora está perfectamente definida para ser empaquetada y distribuida como un repositorio en GitHub para tu amigo.

## 1. Nombre y Descripción de la Habilidad
- **Nombre (Folder/YAML):** `metrology-assistant`
- **Descripción:** "Orquestador paso a paso para la redacción de informes de laboratorio de Metrología (ELI-214). Automatiza la creación del proyecto LaTeX, síntesis de datos experimentales, escritura de scripts en Python, y la auditoría de coherencia transversal."
- **Patrón de Diseño:** *SOP (Standard Operating Procedure) de Orquestación.* Es una habilidad puramente instruccional (no usa un binario CLI propio). En su lugar, el `SKILL.md` maestro actúa como una receta de 11 pasos estrictos que el Agente leerá en el primer prompt y ejecutará iterativamente contigo.

## 2. Estructura de Directorios (El Repositorio de GitHub)

El plugin completo tendrá esta forma al ser descargado por tu amigo:

```text
metrology-assistant/
│
├── plugin.json                 # Metadatos para que Antigravity reconozca el plugin
│
├── skills/
│   └── metrology_report_master/
│       ├── SKILL.md            # El motor principal con los 11 pasos del workflow
│       │
│       ├── resources/
│       │   └── MetrologiaVault/ # Carpeta donde tu amigo subirá las guías y apuntes en PDF/MD
│       │
│       └── templates/
│           ├── main.tex        # Plantilla base LaTeX pre-configurada
│           └── plot_base.py    # Plantilla de matplotlib base para el agente
```

## 3. Estrategia de UX y Consumo de Tokens (Resolución Q1)
- **Token Efficiency:** En lugar de cargar sub-skills gigantes o hacer todo en un solo mega-prompt, el `SKILL.md` dividirá el trabajo en **Fases de Checkpoint**.
- El agente hará la Fase 1, se detendrá y le dirá al usuario: *"Fase 1 completada. ¿Tienes los datos de laboratorio reales (paso 3.1) o quieres que sintetice los datos?"*. Esto ahorra tokens y le da control al usuario.

## 4. El "Vault" (Resolución Q2)
- El agente estará explícitamente instruido en el `SKILL.md` para usar sus herramientas `list_dir` y `view_file` para explorar la ruta local `./resources/MetrologiaVault/` buscando la teoría. Así es 100% portable a cualquier PC.

## 5. Simulación de Datos (Resolución Q3)
- Si el usuario no tiene datos, el agente sintetizará datos perfectos y les agregará ruido/tolerancias calculadas (sin marcarlos como falsos en el reporte). 
- Generará un artefacto `cuadernillo_laboratorio.md` real que tu amigo podrá leer para entender qué datos inventó el agente.

## 6. Ejecución de Scripts (Resolución Q4)
- El agente escribirá todos los códigos en la subcarpeta `<proyecto_latex>/scripts/`.
- El agente usará su herramienta interna `run_command` (terminal) para ejecutar los scripts y generar automáticamente los `.pdf` o `.png` de los gráficos. No requerirá que tu amigo sepa Python.

## 7. Estrategia de Manejo de Errores (Anti-Context Rot)
- En el Paso 11, el agente levantará **Subagentes de fondo** (`invoke_subagent`). Cada subagente recibirá una copia en memoria de la Introducción, Resumen y Conclusión, y los validará contra los Datos Sintetizados de la Fase 2.
- Si un script Python falla (ej: error en matplotlib), el agente leerá el error de la terminal y lo autocorregirá iterativamente hasta que el gráfico exista.

---

## Aprobación Final (Phase 2 Complete)

Si este diseño te parece perfecto, el siguiente paso es que yo **escriba y genere** esta carpeta con el `SKILL.md` y todos sus archivos directamente en tu PC (en la carpeta de plugins) para que la pruebes o la subas a GitHub. 

¿Apruebas este diseño o le hacemos un último ajuste?
