import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear un dataset simulado
print("1. Creación de un dataset simulado")

# Datos de ejemplo
data = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Mouse', 'Teclado'],
    'Precio': [1000, 20, 50, 1050, 22, 48],  # Precios con un valor anómalo
    'Cantidad': [5, 10, 8, 4, 15, 7],
    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Simular un valor nulo y un error
df.loc[2, 'Precio'] = np.nan  # Introducir un valor nulo
df.loc[3, 'Cantidad'] = 0     # Cantidad cero (posible error)

print("\nDataset inicial:")
print(df)

# 2. Guardar y cargar el dataset
print("\n2. Guardar y cargar el dataset")
df.to_csv('data/ventas.csv', index=False)
df_loaded = pd.read_csv('data/ventas.csv')
print("\nDataset cargado desde archivo:")
print(df_loaded)

# 3. Limpieza de datos
print("\n3. Limpieza de datos")

# Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Rellenar valores nulos con la media de la columna 'Precio'
df['Precio'] = df['Precio'].fillna(df['Precio'].mean())
print("\nDataset después de rellenar valores nulos:")
print(df)

# Eliminar filas donde Cantidad es 0
df = df[df['Cantidad'] > 0]
print("\nDataset después de eliminar Cantidad = 0:")
print(df)

# 4. Análisis exploratorio
print("\n4. Análisis exploratorio")

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

# Convertir la columna 'Fecha' a datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])
print("\nPrimeras filas con Fecha como datetime:")
print(df.head())

# 5. Agrupaciones y agregaciones
print("\n5. Agrupaciones y agregaciones")

# Agrupar por Producto y calcular ingresos totales
df['Ingresos'] = df['Precio'] * df['Cantidad']
ventas_por_producto = df.groupby('Producto').agg({'Ingresos': 'sum', 'Cantidad': 'sum'})
print("\nIngresos y Cantidades totales por producto:")
print(ventas_por_producto)

# 6. Visualización
print("\n6. Visualización")

# Gráfico de barras de ingresos por producto
ventas_por_producto['Ingresos'].plot(kind='bar', color='skyblue')
plt.title('Ingresos Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Ingresos ($)')
plt.xticks(rotation=45)
plt.show()

# Gráfico de línea de ingresos a lo largo del tiempo
df = df.sort_values('Fecha')
plt.figure()
plt.plot(df['Fecha'], df['Ingresos'], marker='o')
plt.title('Ingresos a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ingresos ($)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# 7. Experimenta: Filtrado y ordenamiento
print("\n7. Filtrado y ordenamiento")

# Filtrar productos con ingresos > 5000
productos_altos_ingresos = df[df['Ingresos'] > 5000]
print("\nProductos con ingresos > 5000:")
print(productos_altos_ingresos)

# Ordenar por ingresos descendente
df_sorted = df.sort_values('Ingresos', ascending=False)
print("\nDataset ordenado por ingresos:")
print(df_sorted)