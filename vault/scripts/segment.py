import os
import re
from pathlib import Path

def segmentar_apunte(ruta_apunte_original, ruta_second_brain):
    path_apunte = Path(ruta_apunte_original)
    path_brain = Path(ruta_second_brain)
    
    if not path_apunte.exists():
        print(f"Error: No se encuentra el archivo original en {ruta_apunte_original}")
        return

    # Leer el apunte completo de 2500 líneas
    with open(path_apunte, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    # Mapear todas las carpetas existentes en el Second Brain para indexar sus rutas
    mapa_directorios = {}
    for root, dirs, files in os.walk(path_brain):
        for d in dirs:
            # Extraer la numeración inicial (ej: "1.1.1" de "1.1.1 Umbral de percepción")
            match = re.match(r'^([\d\.]+)', d)
            if match:
                mapa_directorios[match.group(1)] = Path(root) / d

    archivo_actual = None
    buffer_contenido = []

    print("Iniciando segmentación del apunte...")

    for linea in lineas:
        # Detectar encabezados de Markdown que contengan la numeración técnica (Ej: "# 1.1" o "## 1.1.1")
        match_header = re.match(r'^#+\s*([\d\.]+)', linea)
        
        if match_header:
            # Guardar el bloque acumulado en el archivo anterior antes de cambiar de sección
            if archivo_actual and buffer_contenido:
                with open(archivo_actual, "a", encoding="utf-8") as f_out:
                    f_out.write("".join(buffer_contenido))
                buffer_contenido = []

            numeracion = match_header.group(1).rstrip('.')
            
            # Buscar la carpeta correspondiente en el mapa del Second Brain
            if numeracion in mapa_directorios:
                ruta_carpeta = mapa_directorios[numeracion]
                # Encontrar el archivo .md dentro de esa carpeta
                for file in os.listdir(ruta_carpeta):
                    if file.endswith(".md"):
                        archivo_actual = ruta_carpeta / file
                        print(f"Escribiendo en: {file}")
                        break
            else:
                # Si el encabezado no coincide con el índice, el contenido se mantiene en la sección actual
                pass
        
        if archivo_actual:
            buffer_contenido.append(linea)

    # Escribir el último bloque remanente
    if archivo_actual and buffer_contenido:
        with open(archivo_actual, "a", encoding="utf-8") as f_out:
            f_out.write("".join(buffer_contenido))

    print("Segmentación e inyección finalizada con éxito.")

if __name__ == "__main__":
    # Configura las rutas exactas de tus archivos aquí
    RUTA_ORIGINAL = r"C:\Users\Jean\Documents\MetrologiaVault\raw\apunte_metrologia\text.md"
    RUTA_BRAIN = r"C:\Users\Jean\Documents\MetrologiaVault\wiki\second_brain"
    
    segmentar_apunte(RUTA_ORIGINAL, RUTA_BRAIN)