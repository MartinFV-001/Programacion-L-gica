# 📊 Proyecto: Análisis de Ventas con Python

Este repositorio contiene dos programas en Python (`ventas.py` y `ventas1.py`) que permiten analizar y visualizar datos de ventas utilizando las librerías `NumPy`, `Pandas` y `Matplotlib`.

## 🧾 Archivos Incluidos

- **ventas.py**  
  Este programa realiza operaciones básicas con arreglos de ventas semanales usando `NumPy`, lee un archivo CSV con datos de productos vendidos y genera una gráfica de barras con `Matplotlib`.

- **ventas1.py**  
  Este segundo programa realiza un análisis más detallado por producto desde el mismo archivo CSV. Muestra estadísticas descriptivas, identifica el producto más y menos vendido, y genera una gráfica circular (pastel) de distribución de ventas.

- **ventas.csv** *(no incluido por privacidad, debe estar en la ruta especificada o cargarse manualmente)*  
  Archivo con los datos de ventas por producto. Debe tener al menos estas columnas:
  - `Producto`
  - `Unidades Vendidas`

## 🛠 Librerías utilizadas

- `NumPy`
- `Pandas`
- `Matplotlib`

Asegúrate de instalarlas si no las tienes:
```bash
pip install numpy pandas matplotlib
