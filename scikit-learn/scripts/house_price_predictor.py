import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Generar datos ficticios
print("1. Generación de datos ficticios")

# Crear datos: tamaño (m²), habitaciones y precio
np.random.seed(42)  # Para reproducibilidad
size = np.random.uniform(50, 200, 100)  # Tamaño entre 50 y 200 m²
rooms = np.random.randint(1, 6, 100)    # Entre 1 y 5 habitaciones
price = 100 * size + 5000 * rooms + np.random.normal(0, 5000, 100)  # Precio simulado

# Crear DataFrame
data = pd.DataFrame({'Tamaño (m²)': size, 'Habitaciones': rooms, 'Precio': price})

# Guardar el dataset en un archivo CSV
data.to_csv('data/houses_data.csv', index=False)
print("\nDataset guardado como 'data/houses_data.csv'")

print("\nPrimeras filas del dataset:")
print(data.head())

# 2. Preparar los datos
print("\n2. Preparación de los datos")

# Características (X) y variable objetivo (y)
X = data[['Tamaño (m²)', 'Habitaciones']]  # Variables independientes
y = data['Precio']  # Variable dependiente

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\nTamaño del conjunto de entrenamiento:", X_train.shape)
print("Tamaño del conjunto de prueba:", X_test.shape)

# 3. Entrenar el modelo
print("\n3. Entrenamiento del modelo")

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Coeficientes del modelo
print("\nCoeficientes del modelo:")
print("Intercepto:", model.intercept_)
print("Coeficiente para Tamaño:", model.coef_[0])
print("Coeficiente para Habitaciones:", model.coef_[1])

# 4. Hacer predicciones
print("\n4. Predicciones")

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test)
print("\nPrimeras predicciones vs valores reales:")
predictions_df = pd.DataFrame({'Real': y_test, 'Predicho': y_pred})
print(predictions_df.head())

# 5. Evaluar el modelo
print("\n5. Evaluación del modelo")

# Calcular métricas
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Coeficiente de Determinación (R²): {r2:.2f}")

# 6. Visualización
print("\n6. Visualización")

# Gráfico de dispersión: Predicciones vs Valores reales
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)  # Línea ideal
plt.title('Predicciones vs Valores Reales')
plt.xlabel('Precio Real ($)')
plt.ylabel('Precio Predicho ($)')
plt.tight_layout()
plt.show()

# 7. Experimenta: Predicción personalizada
print("\n7. Predicción personalizada")
new_house = np.array([[150, 3]])  # Nueva casa: 150 m², 3 habitaciones
predicted_price = model.predict(new_house)
print(f"Precio predicho para una casa de 150 m² con 3 habitaciones: ${predicted_price[0]:.2f}")