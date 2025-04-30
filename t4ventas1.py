# ventas1.py
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
datos = pd.read_csv(r"C:\Tec\Octavo\plyf\Tema1\Tema 4\ventas.csv", encoding='utf-8')

# Mostrar datos generales
print("Resumen de ventas por producto:\n")
print(datos.describe(include='all'))

# Producto con más unidades vendidas
producto_top = datos.loc[datos['Unidades Vendidas'].idxmax()]
print(f"\nProducto más vendido: {producto_top['Producto']} ({producto_top['Unidades Vendidas']} unidades)")

# Producto con menos unidades vendidas
producto_bajo = datos.loc[datos['Unidades Vendidas'].idxmin()]
print(f"Producto menos vendido: {producto_bajo['Producto']} ({producto_bajo['Unidades Vendidas']} unidades)")

# Gráfica circular
plt.pie(datos['Unidades Vendidas'], labels=datos['Producto'], autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Ventas por Producto')
plt.axis('equal')
plt.show()
