import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título del dashboard
st.title('Dashboard de Análisis de Datos')

# Subtítulo y descripción
st.write('Este es un ejemplo básico de un dashboard usando Streamlit.')

# Generar datos ficticios
@st.cache
def generar_datos(num_filas):
    np.random.seed(42)
    datos = pd.DataFrame({
        'Edad': np.random.randint(18, 65, num_filas),
        'Género': np.random.choice(['Masculino', 'Femenino'], num_filas),
        'Ingresos': np.random.normal(50000, 15000, num_filas)
    })
    return datos

num_filas = st.slider('Seleccione el número de filas de datos', min_value=100, max_value=1000, step=100)
datos = generar_datos(num_filas)

# Mostrar los datos en una tabla
st.subheader('Datos Generados')
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
