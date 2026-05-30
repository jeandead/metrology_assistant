# Metrology Assistant - Antigravity Plugin

Este repositorio es un **Plugin para Antigravity**, diseñado como un Orquestador Maestro de 12 Fases para la automatización, cálculo empírico y redacción de informes de laboratorio bajo estándares IEEE (específicamente optimizado para la asignatura ELI-214: Metrología Eléctrica).

## 🚀 Instalación

Este repositorio contiene la "lógica pura" del agente. Para instalarlo en tu ecosistema local de Antigravity:

1. Clona este repositorio en cualquier lugar de tu máquina:
   ```bash
   git clone https://github.com/jeandead/metrology_assistant.git
   ```
2. Navega al directorio:
   ```bash
   cd metrology_assistant
   ```
3. Pide a tu instancia activa de Antigravity que lo instale como un plugin global:
   > *"Instala el plugin ubicado en el directorio actual"*

4. Instala las dependencias subyacentes del sistema (MiKTeX, Python, Git y paquetes pip) requeridas por las templates:
   - Ejecuta el archivo `setup.bat` (puedes darle doble clic desde el Explorador de Archivos o ejecutar `.\setup.bat` en tu terminal).

Antigravity leerá el `plugin.json` y mapeará todas las *skills* internamente.

## ⚙️ Uso Básico

El plugin funciona de manera agnóstica a tus datos. **No trabajes dentro de la carpeta del plugin.** 

1. Crea una carpeta vacía para tu nuevo laboratorio (Ej. `C:\Users\Usuario\Exp_5`).
2. Abre Antigravity en esa carpeta vacía.
3. Invoca la Skill Maestra indicando qué necesitas:
   > *"@metrology-assistant Inicia la fase 1 del protocolo usando la Guía de Experiencia adjunta."*

### 🧠 Modo Autopilot (State-Awareness)

Si ya ejecutaste algunas fases, tienes la guía y los datos medidos (CSV), y quieres que el agente trabaje en bucle profundo hasta tener el PDF compilado, utiliza el comando de meta-meta-orquestación `/goal`:

> *"/goal /metrology-assistant Sigue trabajando en el informe hasta compilar el PDF final."*

El agente hará un escaneo del Filetree local (`tree /F`), identificará automáticamente qué secciones del `.tex` faltan por rellenar, y retomará la ejecución desde la fase exacta correspondiente (ya sea hacer los gráficos en Python, deducir la teoría de Blondel, o concluir los porcentajes de error).

## 📂 Arquitectura del Repositorio (Clean Architecture)

- `/skills`: Contiene la lógica del orquestador y los 12 pasos obligatorios de ejecución.
- `/templates`: Archivos base (ej. `main.tex`, `plotter.py`) que el plugin inyectará automáticamente en tu directorio de trabajo cuando escafoldee un nuevo informe.
- `/agents`: Archivos de configuración de los subagentes especializados (`metrology-auditor`, `metrology-engineer`, `metrology-compiler`).
- `antigravity.md`: Reglas base y constitución del comportamiento del Agente.

## 🛠️ Herramientas de Ingesta (markdown2json)
El sistema requiere el ejecutable `markdown2json.exe` (incluido en `/bin`) para procesar la teoría desde tu Obsidian Vault personal. El agente lo utilizará automáticamente en las Fases 3 y 9 para asegurar que las fórmulas matemáticas LaTeX y la jerarquía de los apuntes no sufran corrupción, lo cual ocurriría si se usara el modelo RAG clásico.

> **💡 Recomendación de Formato:** 
> Cuando necesites pasarle manuales de equipos, guías de laboratorio o papers al agente de Antigravity (para que inicie el protocolo), se recomienda encarecidamente **convertirlos de antemano a formato Markdown (`.md`)**. Subir PDFs directamente puede corromper o perder las ecuaciones matemáticas y las tablas críticas, lo cual afectará la precisión de la Fase 3 (Trabajo Previo).
