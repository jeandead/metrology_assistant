import pandas as pd
import matplotlib.pyplot as plt
import os

"""
PLANTILLA DE ESTILO PARA INFORMES DE INGENIERÍA (IEEE / LAB METROLOGÍA)
----------------------------------------------------------------------
Esta es una guía de estilo para el Agente IA. Al pedir un gráfico, indica: 
"Generar gráfico siguiendo el estilo de src/plotter.py".
"""

# 1. CONFIGURACIÓN DE PARÁMETROS DE ESTILO (rcParams)
# Estos valores garantizan que el gráfico se vea profesional en LaTeX.
plt.rcParams.update({
    "text.usetex": True,             # Habilitado: Usa el motor LaTeX para textos y fórmulas
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman", "Times New Roman"],
    "axes.labelsize": 11,            # Tamaño estándar para etiquetas de ejes
    "axes.titlesize": 11,
    "xtick.labelsize": 9,            # Números de los ejes ligeramente más pequeños
    "ytick.labelsize": 9,
    "figure.titlesize": 12,
    "grid.linewidth": 0.5,
    "grid.alpha": 0.7,
    "lines.linewidth": 1.5           # Líneas claras pero no muy gruesas
})

def generar_grafico_referencia(archivo_csv, salida_png):
    """
    ESTRUCTURA DE REFERENCIA PARA EL AGENTE:
    Al generar un nuevo script, el agente debe seguir esta estructura lógica:
    """
    
    # [A] Preparación: Asegurar directorios (Siempre usar os.makedirs)
    os.makedirs(os.path.dirname(salida_png), exist_ok=True)
    
    # [B] Carga de Datos: Adaptar según la arquitectura del CSV proporcionado
    df = pd.read_csv(archivo_csv)
    
    # [C] Creación de Figura: Usar siempre dpi=300 y el tamaño 6x4 para consistencia
    fig, ax = plt.subplots(figsize=(6, 4), dpi=300)
    
    # [D] Plotting: Usar colores sobrios (Navy #003366, Dark Red #CC0000)
    # Ejemplo: ax.plot(df['X'], df['Y'], label='Leyenda', color='#003366')
    
    # [E] Formato Estricto: Grid punteado y leyenda con borde negro (no redondeado)
    ax.grid(True, which='both', linestyle=':')
    ax.legend(loc='best', frameon=True, edgecolor='black', fancybox=False)
    
    # [F] Exportación: Usar tight_layout y bbox_inches='tight' para LaTeX
    plt.tight_layout()
    plt.savefig(salida_png, bbox_inches='tight')
    plt.close()

# INSTRUCCIÓN PARA EL AGENTE:
# Al ejecutar, el agente debe adaptar esta lógica a las columnas específicas del CSV del usuario.
