import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Conectarse a la base de datos
conn = psycopg2.connect(
    "postgresql://analyst:n5NwBhOz9kEc@ep-soft-king-a5iqrjku.us-east-2.aws.neon.tech/tg"
)

# Consulta SQL para obtener la cantidad total de user_id
query = "SELECT COUNT(user_id) AS total_users FROM users_keys"

# Ejecutar la consulta y obtener los datos en un DataFrame
df = pd.read_sql(query, conn)

# Cerrar la conexión a la base de datos
conn.close()

# Crear el gráfico circular
labels = ['Usuarios', 'Otros']
sizes = [df['total_users'][0], 100 - df['total_users'][0]]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # La relación de aspecto igual asegura que el gráfico sea un círculo.

# Mostrar el gráfico circular en Streamlit
st.title('Cantidad Total de user_id')
st.write(f"La cantidad total de user_id es: {df['total_users'][0]}")
st.pyplot(fig)
