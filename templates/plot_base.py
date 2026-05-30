import matplotlib.pyplot as plt
import numpy as np

# Configuración base para gráficos estilo informe científico
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'figure.figsize': (8, 6),
    'figure.dpi': 300
})

def plot_data():
    # TODO: Inyectar datos aquí
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.1, 3.9, 6.2, 8.1, 10.3])
    
    plt.figure()
    plt.plot(x, y, 'o-', color='#1f77b4', label='Datos experimentales')
    
    plt.title('Título del Gráfico')
    plt.xlabel('Eje X [Unidad]')
    plt.ylabel('Eje Y [Unidad]')
    plt.legend()
    plt.grid(True)
    
    # Guardar figura en PDF para LaTeX
    plt.savefig('../figuras/grafico_base.pdf', bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    plot_data()
