---
name: 01_protocolo_detallado
description: Fase 1 del orquestador maestro. Protocolo Detallado Pre-Laboratorio.
---

# Fase 1: Protocolo Detallado Pre-Laboratorio

## Instrucciones para el Agente
Esta skill se ejecuta **antes** de que el usuario asista al laboratorio físico. Su objetivo es convertir la "Guía de la Experiencia" en un protocolo paso a paso (`protocolo_detallado.tex`) extremadamente riguroso para que el usuario sepa exactamente qué medir y qué botones presionar en los instrumentos.

1. **Recolección de Información:**
   - Pide al usuario que proporcione la Guía de la Experiencia (ej. `Experiencia_XX.md`).
   - Revisa el `vault/` (obligatoriamente `vault/ANTIGRAVITY.md`) para buscar apuntes, manuales de instrumentos (ej. Osciloscopio Rigol) o reglas de seguridad aplicables.

2. **Reglas Metacognitivas del Protocolo (Obligatorias):**
   Al redactar el `protocolo_detallado.tex`, DEBES aplicar sin excepción las siguientes tácticas anti-error del experto metrólogo:
   - **Preparativos Iniciales:** Todo protocolo debe iniciar con una sección que exija iniciar la bitácora anotando las placas de características (Marca, Modelo, Número de Serie e Inventario) de todo instrumento y sonda.
   - **Regla de Oro Anti-AUTO:** Inyecta en negrita la prohibición absoluta de usar el botón físico `AUTO` del osciloscopio en el laboratorio.
   - **Tipografía Estricta:** Usa `\textbf{}` única y exclusivamente para hacer referencia a **botones y perillas físicas** del panel. Usa `\textit{}` para hacer referencia a *softkeys* (teclas de menú de la pantalla digital).
   - **Dualidad de Guardado:** Al pedir al usuario que registre un dato con el osciloscopio, indícale SIEMPRE que guarde la imagen PNG (con el botón físico `Help/Print`) y los datos numéricos CSV (navegando por el menú `Storage`). Además, indícale crear previamente la estructura de carpetas en su pendrive (ej. `ExpX_PasoY`).

3. **Estructuración Estricta por Punto de la Guía (4 Incisos):**
   Por cada sección o experimento solicitado en la Guía de la Experiencia, debes generar un desglose detallado con los siguientes 4 incisos OBLIGATORIOS:
   
   - **Inciso 1: Datos que se deben obtener:** Lista clara y sin ambigüedades de qué variables físicas se van a medir (voltajes, desfases, corrientes).
   - **Inciso 2: Metodología a aplicar:** Explicación metrológica de cómo se va a conectar el circuito y qué método se usará.
   - **Inciso 3: Corroboración con apuntes:** Cruza lo que pide la guía con la teoría de `vault/apunte/`. (Ej: "Según la clase 3, este circuito debería mostrar un desfase de $45^\circ$, esto nos alertará si medimos mal").
   - **Inciso 4: Tutorial exacto del Osciloscopio:** Instrucciones mecánicas extraídas rigurosamente del manual del osciloscopio del Vault, aplicando la Tipografía Estricta y la Dualidad de Guardado.

4. **Inyección del Template:**
   - Puedes leer el template genérico ubicado en la carpeta `templates/protocolo_detallado.tex` de este plugin y usarlo como esqueleto base para inyectar este contenido en el directorio del usuario.
   - Pide validación al usuario antes de compilar y entregar el PDF listo para imprimir o llevar en tablet al laboratorio.
