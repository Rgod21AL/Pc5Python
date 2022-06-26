# Crea una Serie de los numeros 10, 20 and 10.
import pandas as pd
import numpy as np

list=[10,20,30]

s = pd.Series(list)
s
-------------------------------------------------------------------------------------------------
# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
colores=['rojo','verde','azul']
r = pd.Series(colores)
r
-------------------------------------------------------------------------------------------------
# Crea un dataframe vacío llamado 'df'
df = pd.DataFrame()
df
# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
columna = ['Numeros']
df = pd.DataFrame(list, columns=columna)
df
# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df['Colores'] = ['rojo','verde','azul']
df
------------------------------------------------------------------------------------------------
# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
avengers= pd.read_csv('./src/pandas/avengers.csv',sep=',')
avengers.head() #Imprime los 4 primeros
-------------------------------------------------------------------------------------------------
# Muestra las primeras 5 filas del DataFrame.
avengers.head(5) 
# Muestra las primeras 10 filas del DataFrame. 
avengers.head(10) 
# Muestra las últimas 5 filas del DataFrame.
avengers.tail() #Este metodo retorna las ultimas 5 filas
---------------------------------------------------------------------------------------------------
# Muestra el tamaño del DataFrame
avengers.shape
# Muestra los data types del dataframe
avengers.dtypes
---------------------------------------------------------------------------------------------------
# Cambia el indice a la columna "fecha_inicio".
avengers.columns
avengers2 = avengers.set_index("fecha_inicio").copy()
avengers2.head() #Show results
--------------------------------------------------------------------------------------------------
# Ordena el índice de forma descendiente
avengers.index #Con esto vemos el rango de filas
avengers.loc[173:0:-1,['URL','genero']] #Mostramos de manera descendente y esta vez seleccionamos solo 2 columnas
---------------------------------------------------------------------------------------------------------
# Resetea el índice
avengers2.reset_index(drop=True,inplace=True)
avengers2.head() #Show results

