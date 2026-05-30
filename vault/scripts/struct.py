import os
import re
from pathlib import Path

def generar_grafo_anidado(indice_raw, ruta_base=r"C:\Users\Jean\Documents\MetrologiaVault\wiki\second_brain"):
    base_path = Path(ruta_base)
    
    # Estructura de control jerárquico (Nivel 0 es la raíz del Vault)
    historial_rutas = {0: base_path}
    
    # Filtrado inicial de saltos de línea y espacios redundantes
    lineas = [l.strip() for l in indice_raw.strip().split('\n') if l.strip()]
    
    for linea in lineas:
        # Exclusión de metadatos e identificadores de página aislados
        if any(x in linea.upper() for x in ["ÍNDICE GENERAL", "METROLOGÍA ELÉCTRICA", "USM", "JRVM2020"]):
            continue
        if linea.isdigit():
            continue
            
        # 1. Eliminar ráfagas de puntos de relleno (. . . .) preservando puntos divisorios
        linea_limpia = re.sub(r'(\s*\.\s*){2,}', ' ', linea)
        
        # 2. Eliminar numeración de página final flotante
        linea_limpia = re.sub(r'\s+\d+$', '', linea_limpia).strip()
        
        # 3. Clasificación jerárquica por formato numérico
        match_num = re.match(r'^([\d\.]+)\s*(.*)', linea_limpia)
        
        if match_num:
            numeracion = match_num.group(1).rstrip('.')
            titulo = match_num.group(2).strip()
            nivel = len(numeracion.split('.'))
            nombre_nodo = f"{numeracion} {titulo}"
        else:
            # Encabezados de sección principal sin numeración explícita inicial
            nivel = 1
            nombre_nodo = linea_limpia
            
        # 4. Sanitización estricta de strings para sistema de archivos Windows
        nombre_nodo = re.sub(r'[\\/*?:"<>|]', "", nombre_nodo)
        
        # 5. Resolución dinámica de rutas según árbol de dependencias
        parent_path = historial_rutas.get(nivel - 1, base_path)
        ruta_nodo = parent_path / nombre_nodo
        
        # 6. Despliegue en disco de carpetas y archivos markdown nucleares
        ruta_nodo.mkdir(parents=True, exist_ok=True)
        nota_md = ruta_nodo / f"{nombre_nodo}.md"
        
        if not nota_md.exists():
            with open(nota_md, "w", encoding="utf-8") as f:
                f.write(f"# {nombre_nodo}\n\nTags: #eli214\n")
                
        # Actualización del estado del árbol para herencia de subdirectorios
        historial_rutas[nivel] = ruta_nodo

if __name__ == "__main__":
    # Tu string de índice exacto copiado directamente del portapapeles
    indice_metrologia = """
Seguridad Eléctrica
1
1.1. Factores eléctricos sobre las personas . . . . . . . . . . . . . . . . . . . . . . 1
1.1.1. Umbral de percepción . . . . . . . . . . . . . . . . . . . . . . 2
1.1.2. Umbral de reacción . . . . . . . . . . . . . . . . . . . . . . 2
1.1.3. Umbral de no soltar . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.1.4. Umbral de fibrilación ventricular . . . . . . . . . . . . . . . . . . . . 3
1.1.5. Período vulnerable . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.1.6. Curvas inversas . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
1.2. Efectos de una descarga eléctrica sobre las personas . . . . . . . . . . . . . . 6
1.2.1. Marca eléctrica . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.2.2. Quemadura eléctrica . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3. Impedancia del cuerpo humano . . . . . . . . . . . . . . . . . . . . . . . . . 7
1.4. Factor de corriente de corazón . . . . . . . . . . . . . . . . . . . . . . . . . . 11
1.5. Seguridad eléctrica en las instalaciones . . . . . . . . . . . . . . . . . . . . . 12
1.5.1. Riesgos Eléctricos . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
1.5.2. Diferencias entre neutro y tierra . . . . . . . . . . . . . . . . . . . . . 16
1.6. Sistemas de puesta a tierra . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
1.6.1. Conexión a tierra de las carcasas y estructuras . . . . . . . . . . . . . 21
1.7. Protecciones eléctricas domiciliarias . . . . . . . . . . . . . . . . . . . . . . 22
1.7.1. Interruptor termomagnético . . . . . . . . . . . . . . . . . . . . . . . 22
1.7.2. Interruptor diferencial . . . . . . . . . . . . . . . . . . . . . . . . . 25
Errores y Análisis de Datos
27
2.1. Prolegómenos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.1.1. Definiciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
2.1.2. Elementos que intervienen en una medición . . . . . . . . . . . . . . 28
2.1.3. Proceso de medición de variables (eléctricas) . . . . . . . . . . . . . 28
2.2. Definiciones en metrología . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
2.3. Análisis de errores y su propagación . . . . . . . . . . . . . . . . . . . . . . 36
2.3.1. Tipos de errores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
2.3.2. Error Admisible en Instrumentos de Indicación Analógica . . . . . . 38
2.3.3. Error Admisible en Instrumentos de Indicación Digital . . . . . . . . 39
2.3.4. Error Admisible en Instrumentos de Pantalla Reticulada . . . . . . . 40
2.3.5. Incertidumbre de una Medición . . . . . . . . . . . . . . . . . . . . . 41
2.3.6. Intervalo de confianza . . . . . . . . . . . . . . . . . . . . . . . . . . 43
2.3.7. Propagación de errores e incertidumbres . . . . . . . . . . . . . . . . 50
2.3.8. Propagación de incertidumbres . . . . . . . . . . . . . . . . . . . . . 51
2.3.9. Resultado de una medición . . . . . . . . . . . . . . . . . . . . . . . 53
2.4. Cifras significativas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
2.4.1. Aproximaciones en mediciones . . . . . . . . . . . . . . . . . . . . . 56
2.4.2. Operaciones considerando cifras significativas . . . . . . . . . . . . . 57
2.5. Sistema de Unidades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
2.6. Tabla para expandir incertidumbres . . . . . . . . . . . . . . . . . . . . . . . 61
Osciloscopio
62
3.1. Prolegómenos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
3.2. Principio de Funcionamiento . . . . . . . . . . . . . . . . . . . . . . . . . . 64
3.2.1. Osciloscopio analógico . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.2.2. Funcionamiento osciloscopio digital . . . . . . . . . . . . . . . . . . 75
3.3. Barrido horizontal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
3.3.1. Señal de barrido sin sincronía . . . . . . . . . . . . . . . . . . . . . . 77
3.3.2. Señal de barrido sincronizada . . . . . . . . . . . . . . . . . . . . . . 78
3.3.3. Definición de Trigger y sus condiciones. . . . . . . . . . . . . . . . . 79
3.4. Modo de acoplamiento de los canales de entrada . . . . . . . . . . . . . . . 82
3.5. Puntas del Osciloscopio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
Medición de Tensión y Corriente Continua
85
4.1. Introducción y definiciones . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
4.1.1. Definiciones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.1.2. Descomposición de señales . . . . . . . . . . . . . . . . . . . . . . . 87
4.1.3. Respuesta en frecuencias y filtros . . . . . . . . . . . . . . . . . . . . 89
4.2. Modelos eléctricos de voltímetros y amperímetros . . . . . . . . . . . . . . . 93
4.2.1. Voltímetro ideal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
4.2.2. Amperímetro ideal . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
4.3. Instrumentos analógicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
4.3.1. Instrumento de bobina móvil . . . . . . . . . . . . . . . . . . . . . . 95
4.3.2. Amperímetro de bobina móvil . . . . . . . . . . . . . . . . . . . . . . 98
4.3.3. Voltímetro de bobina móvil . . . . . . . . . . . . . . . . . . . . . . . 101
4.4. Instrumentos electrónicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
4.4.1. Voltímetro y amperímetro electrónico . . . . . . . . . . . . . . . . . 105
4.4.2. Introducción a la conversión analógica-digital . . . . . . . . . . . . . 109
4.4.3. Ampliación del rango de medida . . . . . . . . . . . . . . . . . . . . 114
4.4.4. Influencia sobre el circuito a medir . . . . . . . . . . . . . . . . . . . 115
4.4.5. Electrómetro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
4.5. Medición de resistencia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
4.5.1. Medición por voltímetro-amperímetro . . . . . . . . . . . . . . . . . 116
4.5.2. Óhmetro de bobina móvil . . . . . . . . . . . . . . . . . . . . . . . . 120
4.5.3. Óhmetro de bobinas cruzadas . . . . . . . . . . . . . . . . . . . . . . 122
4.5.4. Óhmetro electrónico . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
4.5.5. Medición por comparación . . . . . . . . . . . . . . . . . . . . . . . . 124
4.5.6. Medición por puente . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
Medición de Tensión y Corriente Alterna
128
5.1. Introducción y definiciones . . . . . . . . . . . . . . . . . . . . . . . . . . . 128
5.1.1. Espectro y respuesta en frecuencia . . . . . . . . . . . . . . . . . . . 129
5.1.2. Decibeles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
5.1.3. Trabajo con respuesta en frecuencia . . . . . . . . . . . . . . . . . . 132
5.1.4. Diagrama Logarítmico o de Bode . . . . . . . . . . . . . . . . . . . . 133
5.1.5. Diagrama de Bode para los factores elementales. . . . . . . . . . . . 135
5.2. Respuesta en frecuencia de un instrumento . . . . . . . . . . . . . . . . . . 140
5.3. Instrumento de fierro móvil . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
5.3.1. Principio de funcionamiento . . . . . . . . . . . . . . . . . . . . . . . 143
5.3.2. Voltímetro y amperímetro de fierro móvil . . . . . . . . . . . . . . . 145
5.4. Instrumento de bobina móvil con rectificador . . . . . . . . . . . . . . . . . 145
5.4.1. Instrumento con rectificador media de onda . . . . . . . . . . . . . . 146
5.4.2. Instrumento con rectificador onda completa . . . . . . . . . . . . . . 148
5.5. Instrumentos de valor máximo . . . . . . . . . . . . . . . . . . . . . . . . . 150
5.6. Voltímetros electrónicos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 151
5.6.1. Principio de funcionamiento . . . . . . . . . . . . . . . . . . . . . . . 151
5.6.2. Atenuador del voltímetro . . . . . . . . . . . . . . . . . . . . . . . . 152
Medición de Potencia, Factor de Potencia y Energía
154
6.1. Introducción . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
6.2. Medición de potencia monofásica a frecuencia industrial . . . . . . . . . . . 158
6.2.1. Generalidades . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
6.2.2. Instrumentos para medir potencia activa . . . . . . . . . . . . . . . . 159
6.2.3. Modelo y conexiones del vatímetro . . . . . . . . . . . . . . . . . . . 161
6.2.4. Ampliación de rangos . . . . . . . . . . . . . . . . . . . . . . . . . . 162
6.2.5. Medición de potencia reactiva . . . . . . . . . . . . . . . . . . . . . . 163
6.3. Medición de potencia trifásica . . . . . . . . . . . . . . . . . . . . . . . . . . 163
6.3.1. Teorema de Blondel y el vatímetro trifásico . . . . . . . . . . . . . . 163
6.3.2. Medición de potencia trifásica circuitos trifilares . . . . . . . . . . . . 165
6.3.3. Ejemplo de circuito desbalanceado. . . . . . . . . . . . . . . . . . . . 167
6.3.4. Medición de potencia trifásica circuitos tetrafilares . . . . . . . . . . 172
6.3.5. Medición de potencia reactiva trifásica . . . . . . . . . . . . . . . . . 172
6.4. Medición del factor de potencia a frecuencia industrial . . . . . . . . . . . . 173
6.4.1. Cosfímetro de bobinas cruzadas . . . . . . . . . . . . . . . . . . . . . 173
6.4.2. Cosfímetro de bobinas fierro móvil . . . . . . . . . . . . . . . . . . . 174
6.4.3. Cosfímetro electrónico . . . . . . . . . . . . . . . . . . . . . . . . . . 174
6.4.4. Factor de potencia en redes trifásicas . . . . . . . . . . . . . . . . . . 176
6.5. Medición de energía . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
6.5.1. Ejercicio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
"""
    generar_grafo_anidado(indice_metrologia)
    print("Estructura jerárquica de Obsidian construida exitosamente.")