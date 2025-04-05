import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Crear un dataset simulado
print("1. Creación de un dataset simulado")

# Generar datos
np.random.seed(42)  # Para reproducibilidad
data = {
    'Edad': np.random.randint(18, 25, 100),  # Edades entre 18 y 24
    'Horas_Estudio': np.random.uniform(1, 10, 100),  # Horas de estudio entre 1 y 10
    'Nota': np.random.normal(75, 10, 100).clip(0, 100),  # Notas con media 75 y desviación 10
    'Genero': np.random.choice(['Masculino', 'Femenino'], 100)  # Género aleatorio
}

# Crear un DataFrame
df = pd.DataFrame(data)

# Introducir algunos valores atípicos para análisis
df.loc[5:10, 'Nota'] = df.loc[5:10, 'Nota'] + 20  # Aumentar notas para simular outliers
df.loc[90:95, 'Horas_Estudio'] = df.loc[90:95, 'Horas_Estudio'] * 1.5  # Más horas para algunos

print("\nPrimeras filas del dataset:")
print(df.head())

# 2. Configurar el estilo de Seaborn
print("\n2. Configuración del estilo")
sns.set_style("whitegrid")  # Estilo de fondo con rejilla

# 3. Visualizaciones con Seaborn
plt.figure(figsize=(15, 10))

# 3.1 Histograma de notas
print("\n3.1 Histograma de notas")
plt.subplot(2, 2, 1)
sns.histplot(data=df, x='Nota', bins=20, kde=True, color='skyblue')
plt.title('Distribución de Notas')
plt.xlabel('Nota')
plt.ylabel('Frecuencia')

# 3.2 Gráfico de dispersión (Nota vs Horas de Estudio)
print("\n3.2 Gráfico de dispersión (Nota vs Horas de Estudio)")
plt.subplot(2, 2, 2)
sns.scatterplot(data=df, x='Horas_Estudio', y='Nota', hue='Genero', size='Edad', alpha=0.6)
plt.title('Relación entre Horas de Estudio y Notas')
plt.xlabel('Horas de Estudio')
plt.ylabel('Nota')

# 3.3 Boxplot de notas por género
print("\n3.3 Boxplot de notas por género")
plt.subplot(2, 2, 3)
sns.boxplot(data=df, x='Genero', y='Nota', palette='pastel')
plt.title('Distribución de Notas por Género')
plt.xlabel('Género')
plt.ylabel('Nota')

# 3.4 Mapa de calor de correlación
print("\n3.4 Mapa de calor de correlación")
plt.subplot(2, 2, 4)
correlation_matrix = df[['Edad', 'Horas_Estudio', 'Nota']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriz de Correlación')

# Ajustar el layout
plt.tight_layout()
plt.show()

# 4. Experimenta: Filtrado y visualización personalizada
print("\n4. Filtrado y visualización personalizada")

# Filtrar estudiantes con notas > 80
df_high_notes = df[df['Nota'] > 80]

# Gráfico de dispersión personalizado
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df_high_notes, x='Horas_Estudio', y='Nota', hue='Genero', style='Genero', s=100)
plt.title('Estudiantes con Notas > 80')
plt.xlabel('Horas de Estudio')
plt.ylabel('Nota')
plt.legend(title='Género')
plt.show()