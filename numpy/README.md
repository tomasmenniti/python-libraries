## Analizador de Datos Numéricos con NumPy:

    Este script genera datos aleatorios (como alturas de personas), realiza operaciones matemáticas 
    y estadísticas con NumPy, y muestra resultados. También incluye visualización básica usando Matplotlib.



## Instalación 
    pip install numpy matplotlib



## Información al ejecutar el código:

    - Array de alturas aleatorias.

    - Resultados de operaciones matemáticas y matriciales.

    - Estadísticas descriptivas.

    - Histograma (Matplotlib).

    - Datos filtrados y guardados/cargados.



## Explicación:

    - Creación de arrays:

        np.random.uniform para generar datos aleatorios y reshape para reorganizarlos en matrices.

    - Operaciones matemáticas:

        Las operaciones como sumar o multiplicar se aplican elemento por elemento (broadcasting).

    - Operaciones matriciales:

        np.dot y np.eye, (álgebra lineal).

    - Estadísticas:

        np.mean, np.median y np.std (análisis de datos).

    - Visualización:

        El histograma muestra la distribución de los datos.

    - Filtrado:

        Indexación booleana (heights > 180) para procesar datos.

    - Guardado y carga:

        Guardado y recuperación de datos.