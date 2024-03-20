import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Título del dashboard
st.title('Dashboard de Análisis de Datos')

# Subtítulo y descripción
st.write('Este es un ejemplo básico de un dashboard usando Streamlit.')

# Cargar datos (por ejemplo, un archivo CSV)
@st.cache
def cargar_datos():
    datos = pd.read_csv('datos.csv')
    return datos

datos = cargar_datos()

# Mostrar los datos en una tabla
st.subheader('Datos')
st.write(datos)

# Gráfico de barras
st.subheader('Gráfico de Barras')
columna = st.selectbox('Seleccione una columna para visualizar', options=datos.columns)
conteo_valores = datos[columna].value_counts()
plt.bar(conteo_valores.index, conteo_valores)
plt.xlabel(columna)
plt.ylabel('Frecuencia')
st.pyplot()

# Gráfico de dispersión
st.subheader('Gráfico de Dispersión')
x = st.selectbox('Seleccione una columna para el eje X', options=datos.columns)
y = st.selectbox('Seleccione una columna para el eje Y', options=datos.columns)
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x, y=y, data=datos)
st.pyplot()
