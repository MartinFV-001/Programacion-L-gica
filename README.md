# 📊 Prácticas de Análisis de Datos y Clasificación en Python

Este repositorio contiene varios programas escritos en Python que permiten analizar datos, generar gráficas y construir modelos de clasificación usando librerías como `NumPy`, `Pandas`, `Matplotlib` y `scikit-learn`.

## 🧾 Archivos Incluidos

- **ventas.py**  
  Realiza operaciones básicas con arreglos de ventas semanales usando `NumPy`, lee un archivo CSV con datos de productos vendidos y genera una gráfica de barras con `Matplotlib`.

- **ventas1.py**  
  Análisis más detallado por producto desde el mismo archivo CSV. Muestra estadísticas descriptivas, identifica el producto más y menos vendido, y genera una gráfica circular (pastel) de distribución de ventas.

- **ventas.csv** *(no incluido por privacidad)*  
  Archivo con los datos de ventas por producto. Debe tener al menos las columnas:
  - `Producto`
  - `Unidades Vendidas`

- **t4ventas.py**  
  Analiza datos de empleados desde un archivo CSV, calcula bonos, y genera gráficas de salarios. Se centra en productividad y compensaciones.

- **t4ventas1.py**  
  Versión alternativa o extendida del análisis anterior. Puede incluir otras métricas o gráficas más específicas para complementar el análisis de `t4ventas.py`.

- **t4flores.py**  
  Clasificador que utiliza el dataset Iris para predecir especies de flores usando regresión logística. Divide los datos en entrenamiento (70%) y prueba (30%), entrena el modelo y muestra su precisión.

- **t4vinos.py**  
  Clasificador basado en el dataset de vinos de `scikit-learn`. Utiliza regresión logística para predecir el tipo de vino. Divide los datos en entrenamiento (80%) y prueba (20%) y evalúa la precisión del modelo.

- **empleados.py**  
  Genera el archivo `empleados.csv` con datos ficticios de 30 empleados, incluyendo nombre, edad, departamento y salario.

- **prueba.py**  
  Archivo auxiliar utilizado para pruebas generales de código. Puede contener experimentos con funciones de `Pandas`, `NumPy` o `Matplotlib`.

- **requirements.txt**  
  Contiene las versiones exactas de las librerías utilizadas (`numpy`, `pandas`, `matplotlib`), útil para replicar el entorno de trabajo.

- **empleados.csv**  
  Archivo con los datos generados por `empleados.py`. Incluye columnas como `Nombre`, `Edad`, `Departamento` y `Salario`.

## 🛠 Librerías utilizadas

- `NumPy`
- `Pandas`
- `Matplotlib`
- `scikit-learn`

### Instalación rápida de dependencias

```bash
pip install -r requirements.txt
