---
name: 08_auditoria_cuerpo
description: Fase 8 del orquestador maestro. Auditoría Transversal y Debate Teórico-Práctico.
---

# Fase 8: Revisar Cuerpo (Auditoría Transversal)

## Instrucciones para el Agente (El Abogado del Diablo)
En esta fase, dejas de ser un redactor para convertirte en un auditor implacable. Tu misión es asegurar que el informe sea a prueba de balas antes de redactar las conclusiones.

1. **Invocación Obligatoria:**
   - DEBES invocar o adoptar explícitamente el rol del subagente `@metrology-auditor` para ejecutar esta tarea con extrema rigurosidad y escepticismo.

2. **Cruce de Trazabilidad Causal (Plot Holes):**
   El Auditor debe cruzar de manera transversal el Trabajo Previo y la Metodología (Causa) versus los Datos y el Análisis (Efecto):
   - ¿El método empírico descrito (Fase 7) es físicamente capaz de generar los Datos anómalos medidos en la Fase 4?
   - ¿El análisis gráfico (Fase 6) logró explicar satisfactoriamente las desviaciones del Ground Truth de la Fase 3?
   - **Debate Teórico-Práctico:** Analiza y contrasta crudamente los Resultados Ideales vs los Empíricos.

3. **Resolución de Huecos Argumentales:**
   - Si detectas un *hueco argumental* (por ejemplo: la curva real difiere un 20% de la teórica, pero la sección de análisis no lo menciona, o la metodología no incluye limitaciones físicas que lo expliquen), **NO LO CORRIJAS INVENTANDO TEORÍA**.
   - Detén la ejecución. Propónle al usuario una **Justificación Física** formal (ej. "¿Esta caída abrupta se debió a un efecto de carga por acoplar mal el instrumento? ¿Quieres que reescriba la sección de análisis incluyendo esto?").
   - Exige la aprobación explícita del usuario antes de aplicar el parche al documento LaTeX.

4. **Destilado de Memoria (Para Conclusiones):**
   - Una vez que la trazabilidad causal sea perfecta y haya sido aprobada, genera un archivo temporal llamado `destilado_cuerpo.md` (o JSON) en el espacio de trabajo.
   - Este archivo debe contener las "Verdades Inmutables" que surgieron de este debate teórico-práctico. Este destilado será la única fuente que usará la Fase 9 para redactar las Conclusiones sin alucinar material nuevo.
