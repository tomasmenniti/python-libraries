## Sobre scikit-learn:

    Biblioteca de código abierto en Python diseñada para machine learning. Proporciona herramientas simples y eficientes para:

    Clasificación: Predecir categorías (por ejemplo, si un correo es spam o no).

    Regresión: Predecir valores numéricos continuos (como precios de casas).

    Clustering: Agrupar datos sin etiquetas predefinidas.

    Preprocesamiento: Limpiar y transformar datos (escalado, codificación, etc.).

    Evaluación: Medir el rendimiento de los modelos (precisión, error, etc.).



## Predicción de Precios de Casas con Scikit-learn:

    Este proyecto genera datos ficticios sobre casas (tamaño en m², número de habitaciones y precio) y utiliza Scikit-learn para entrenar un modelo de regresión lineal que prediga los precios. Incluye preprocesamiento básico, entrenamiento, evaluación y visualización.



## Instalación 
    pip install numpy pandas scikit-learn matplotlib



## Información al ejecutar el código:

    - Un dataset inicial con 100 casas.

    - Detalles del modelo (coeficientes, predicciones).

    - Métricas de evaluación (MSE y R²).

    - Un gráfico comparando precios reales y predichos.

    - Una predicción personalizada.



## Explicación:

    - Generación de datos ficticios: 
    
        Dataset simple con NumPy y Pandas para simular casas con tamaño, habitaciones y precios.

    - Preparación de los datos:

        train_test_split divide los datos en entrenamiento (80%) y prueba (20%) (evaluación del modelo).

        Separa las características (X) de la variable objetivo (y).

    - Entrenamiento del modelo: 

        LinearRegression() crea un modelo de regresión lineal.

        fit() entrena el modelo con los datos de entrenamiento, ajustando los coeficientes.

    - Predicciones: 

        predict() usa el modelo entrenado para estimar precios en el conjunto de prueba.

    - Evaluación del modelo: 

        mean_squared_error mide el error promedio.

        r2_score indica qué tan bien el modelo explica la variabilidad de los datos (1 es perfecto, 0 o menos indica un mal ajuste).

    - Visualización: 
    
        Un gráfico de dispersión compara los valores reales con las predicciones, ayudándote a ver el rendimiento visualmente.

    - Predicción personalizada: 
    
        Permite probar el modelo con nuevos datos, reforzando su uso práctico.