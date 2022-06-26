import pandas as pd
df_airbnb = pd.read_csv("./src/pandas/airbnb.csv") #-->DATAFRAME

#CASO 1
cond = (df_airbnb.reviews>10) & (df_airbnb.overall_satisfaction>4) & (df_airbnb.bedrooms>4)
#columnas = ['reviews','overall_satisfaction','bedrooms']
df_filtros = df_airbnb[cond] #creamos una nueva variable para evitar confusiones
df_filtros #df_filtros[columnas] -->Para mostrar la data solo con las columnas ingresadas
#Ordenamos segun lo pedido 
final_data = df_filtros.sort_values(by=["overall_satisfaction","reviews"], ascending=[False, False])
#Mostramos 3 alternativas
final_data.head(3) #-->Mostramos las 3 alternativas

#CASO 2
#Cambiamos de indice
df_airbnb2 = df_airbnb.set_index("room_id").copy()
#Buscamos las ID pedidas
new_data = df_airbnb2.loc[[90387,97503]]
#Reseatemos los indices
new_data.reset_index(drop=True, inplace=True)
new_data['room_id'] = [90387,97503] #--->Agregamos la columna del 'room_id'
new_data
#Exportamos como excel
new_data.to_excel('./src/pandas/roberto.xlsx',
            sheet_name='data',encoding='utf-8',index=False) 
            #Ese index = 'false' hace que no se muestren los indices

#CASO 3
cond = (df_airbnb.price<50) 
data = df_airbnb[cond]
#Ordenamos de manera ascendente segun el precio y puntuacion
df_cheaper = data.sort_values(by=["price","room_type","overall_satisfaction"], ascending=[True,False,False])
df_cheaper.head(10)

#CASO 1 UTILIZANDO MATPLOT
#Realizar un gráfico circular, de la cantidad de tipo de habitaciones 'room_type'

df_airbnb.room_type.value_counts().plot.pie()

