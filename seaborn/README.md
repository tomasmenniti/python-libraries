## Analizador Visual de Datos de Estudiantes con Seaborn:

    Este script simula un dataset con información de estudiantes (notas, horas de estudio, edades y género) y utiliza Seaborn para crear visualizaciones estadísticas como histogramas, gráficos de dispersión, cajas (boxplots) y mapas de calor.



## Instalación 
    pip install pandas numpy seaborn matplotlib



## Información al ejecutar el código:

    - Dataset inicial con 100 estudiantes.

    - Gráfico compuesto de 2x2 con:

        Histograma de notas.

        Gráfico de dispersión de notas vs horas de estudio.

        Boxplot de notas por género.

        Mapa de calor de correlación.

    - Un segundo gráfico de dispersión para estudiantes con notas > 80.



## Explicación:

    - Creación de un dataset simulado: 
    
        Se utiliza Pandas y NumPy para generar datos realistas con algunas anomalías (outliers) para practicar el análisis visual.

    - Configuración del estilo: 
    
        sns.set_style() permite personalizar el aspecto de los gráficos (ventaja de Seaborn sobre Matplotlib).

    - Visualizaciones con Seaborn:

        Histograma (sns.histplot): 

            Muestra la distribución de notas con una curva de densidad (kde) para entender la forma de los datos.

        Gráfico de dispersión (sns.scatterplot): 
        
            Explora la relación entre horas de estudio y notas, con codificación por género y tamaño por edad.

        Boxplot (sns.boxplot): 
        
            Compara la distribución de notas por género, destacando medianas, cuartiles y outliers.

        Mapa de calor (sns.heatmap): 
        
            Visualiza la correlación entre variables numéricas (análisis de datos).

    - Filtrado y personalización: 
    
        Filtrado de datos y creación de gráfico adicional (segmentación y ajustes estéticos).