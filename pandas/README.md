## Analizador de Datos de Ventas con Pandas:

    Este script simula un dataset de ventas (productos, precios, cantidades y fechas) y utiliza Pandas para 
    cargarlo, limpiarlo, analizarlo y visualizarlo.



## Instalación 
    pip install pandas matplotlib



## Información al ejecutar el código:

    - Dataset inicial con datos simulados.

    - Resultados después de limpieza (valores nulos rellenados, filas con Cantidad = 0 eliminadas).

    - Estadísticas descriptivas y tablas de ingresos por producto.

    - Dos gráficos: uno de barras para ingresos por producto y otro de línea para ingresos por fecha.



## Explicación:

    - Creación de un dataset simulado: 
    
        Diccionario para crear un DataFrame (la estructura principal de Pandas). (Organización de datos en 
        filas y columnas).

    - Guardar y cargar datos: 
    
        Persistencia y recuperación de datos con to_csv y read_csv.

    - Limpieza de datos: 
    
        isnull().sum() identifica valores nulos.

        fillna() y filtros (df[df['Cantidad'] > 0]) (manejo de datos incompletos o erróneos).

    - Análisis exploratorio: 

        describe() para estadísticas rápidas (media, máximo, mínimo, etc.).

        to_datetime() para convertir cadenas en fechas.

    - Agrupaciones y agregaciones: 

        groupby() y agg() para resumir datos por categorías.

    - Visualización: 
    
        Matplotlib + Pandas para crear gráficos de barras y líneas.

    - Filtrado y ordenamiento: 
    
        Filtros y sort_values (para extraer subconjuntos de datos y ordenarlos).