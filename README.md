# 📊 Practicas

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

- **t4ventas.py**  
  Script que analiza datos de empleados desde un archivo CSV, calcula bonos, y genera gráficas de salarios. Se centra en tareas relacionadas con productividad y compensaciones.

- **t4ventas1.py**  
  Versión alternativa o extendida del análisis anterior. Puede incluir otras métricas o gráficas más específicas para complementar el análisis de `t4ventas.py`.

- **empleados.py**  
  Script que genera el archivo `empleados.csv` con datos ficticios de 30 empleados, incluyendo nombre, edad, departamento y salario.

- **prueba.py**  
  Archivo auxiliar utilizado para pruebas generales de código. Puede contener fragmentos o experimentos con funciones de Pandas, NumPy o Matplotlib.

- **requirements.txt**  
  Archivo que contiene las versiones exactas de las librerías utilizadas (`numpy`, `pandas`, `matplotlib`), útil para replicar el entorno de trabajo.

- **empleados.csv**  
  Archivo con los datos generados por `empleados.py`. Incluye columnas como `Nombre`, `Edad`, `Departamento` y `Salario`.

## 🛠 Librerías utilizadas

- `NumPy`
- `Pandas`
- `Matplotlib`

Asegúrate de instalarlas si no las tienes:
```bash
pip install numpy pandas matplotlib
