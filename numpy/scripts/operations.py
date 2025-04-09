import numpy as np
import matplotlib.pyplot as plt

# 1. Crear arrays con NumPy
print("1. Creación y manipulación de arrays")

# Crear un array de 1 dimensión (vector) con 10 números aleatorios entre 0 y 100
heights = np.random.uniform(150, 200, 10)  # Alturas en cm (entre 150 y 200)
print("Alturas generadas (en cm):", heights)

# Convertir a array de 2 dimensiones (matriz) para simular datos organizados
heights_matrix = heights.reshape(2, 5)  # Reorganiza en 2 filas y 5 columnas
print("\nMatriz de alturas (2x5):")
print(heights_matrix)

# 2. Operaciones matemáticas con NumPy
print("\n2. Operaciones matemáticas")

# Sumar 10 cm a todas las alturas
heights_plus_10 = heights + 10
print("Alturas después de sumar 10 cm:", heights_plus_10)

# Multiplicar todas las alturas por 1.5 (simulando un factor de crecimiento)
heights_scaled = heights * 1.5
print("Alturas escaladas (x1.5):", heights_scaled)

# 3. Operaciones matriciales
print("\n3. Operaciones matriciales")

# Multiplicar matrices (ejemplo: heights_matrix por una matriz identidad)
identity_matrix = np.eye(2)  # Matriz identidad 2x2
result_matrix = np.dot(identity_matrix, heights_matrix)  # Producto de matrices
print("Resultado de multiplicar la matriz por la identidad:")
print(result_matrix)

# Transponer la matriz
transposed_matrix = heights_matrix.T
print("\nMatriz transpuesta:")
print(transposed_matrix)

# 4. Cálculos estadísticos
print("\n4. Estadísticas con NumPy")

# Calcular media, mediana, desviación estándar y máximo/mínimo
mean_height = np.mean(heights)
median_height = np.median(heights)
std_height = np.std(heights)
max_height = np.max(heights)
min_height = np.min(heights)

print(f"Media de alturas: {mean_height:.2f} cm")
print(f"Mediana de alturas: {median_height:.2f} cm")
print(f"Desviación estándar: {std_height:.2f} cm")
print(f"Máximo: {max_height:.2f} cm")
print(f"Mínimo: {min_height:.2f} cm")

# 5. Visualización (opcional, pero útil para entender datos)
print("\n5. Visualización de datos")

# Crear un histograma de las alturas
plt.hist(heights, bins=5, color='blue', alpha=0.7)
plt.title("Distribución de Alturas")
plt.xlabel("Altura (cm)")
plt.ylabel("Frecuencia")
plt.grid(True)
plt.show()

# 6. Experimenta: Filtrar datos
print("\n6. Filtrado de datos")

# Filtrar alturas mayores a 180 cm
tall_people = heights[heights > 180]
print("Personas con altura > 180 cm:", tall_people)

# 7. Guardar y cargar datos (opcional)
print("\n7. Guardar y cargar arrays")

# Guardar el array en un archivo .npy
np.save('data/heights_data.npy', heights)

# Cargar el array desde el archivo
loaded_heights = np.load('data/heights_data.npy')
print("Alturas cargadas desde archivo:", loaded_heights)