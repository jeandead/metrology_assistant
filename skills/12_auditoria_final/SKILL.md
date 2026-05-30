---
name: 12_auditoria_final
description: Fase 12 del orquestador maestro. Auditoría Mecánica de Compilación.
---

# Fase 12: Auditoría Mecánica y Compilación Final

## Instrucciones para el Agente (El Compilador)
En esta fase, la discusión teórica ha terminado. El informe es ahora un bloque de software que debe compilar a la perfección. Tu misión es depurar cualquier error de sintaxis y referencias rotas.

1. **Invocación Oficial de `@metrology-compiler`:**
   - Adopta o delega explícitamente las siguientes tareas al subagente experto en dependencias y compilación.

2. **Auditoría de Codificación (UTF-8 Estricto):**
   - El idioma de este informe es el español. Un error de tildes o eñes corromperá el PDF. 
   - El compilador debe asegurar que TODOS los archivos `.tex` y `.md` manipulados en el directorio de trabajo estén guardados explícitamente bajo codificación UTF-8 (sin BOM).

3. **Linter de Dependencias y Huérfanos:**
   - Rastrea el árbol de `main.tex` y todos sus archivos `_main.tex` anidados.
   - **Regla Anti-Huérfanos:** Detecta y alerta si hay archivos en la carpeta `sections/` que nunca fueron incluidos vía `\input{}`, o si existen comandos `\input{}` apuntando a archivos fantasmas.
   - Audita que todas las llamadas `\includegraphics{}` apunten a rutas y archivos válidos.

4. **Linter de Referencias Cruzadas:**
   - Escanea el documento en busca de etiquetas huérfanas o rotas. Todo `\autoref{}` debe tener su contraparte `\label{}` debidamente instanciada en el código. Esto evita los molestos símbolos `??` en el PDF final.

5. **Loop de Compilación Forzosa (Doble Pasada):**
   - Una vez que la sintaxis esté limpia, invoca o pide autorización para lanzar el comando de compilación (`pdflatex`).
   - **REGLA DE ORO LATEX:** DEBES ejecutar el comando de compilación al menos **dos veces consecutivas**. La primera pasada genera los archivos auxiliares (.aux, .toc) y la segunda pasada construye los índices visuales (TOC, LOF, LOT).
   - Utiliza el loop de 5 intentos autónomos si necesitas arreglar dependencias menores antes de reportar un fallo catastrófico.

6. Reporta el estado de "Ready to Publish" al usuario.
