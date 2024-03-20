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
df_user_id = pd.read_sql(query, conn)

# Cerrar la conexión a la base de datos después de obtener la primera consulta
conn.close()

# Mostrar el resultado en un gráfico
st.title('Cantidad Total de user_id')
st.write(f"La cantidad total de user_id es: {df_user_id['total_users'][0]}")

# Volver a conectar a la base de datos para la siguiente consulta
conn = psycopg2.connect(
    "postgresql://analyst:n5NwBhOz9kEc@ep-soft-king-a5iqrjku.us-east-2.aws.neon.tech/tg"
)

# Consulta SQL para obtener los datos
query2 = "SELECT source, source_url, COUNT(id) as count FROM resumes GROUP BY source, source_url"

# Ejecutar la consulta y obtener los datos en un DataFrame
df_resumes = pd.read_sql(query2, conn)

# Calcular porcentajes para source_url
total_source_url = df_resumes[df_resumes['source'] == 'source_url']['count'].sum()
percentage_source_url = (df_resumes[df_resumes['source'] == 'source_url']['count'] / total_source_url) * 100

# Calcular porcentajes para source
total_source = df_resumes[df_resumes['source'] == 'source']['count'].sum()
percentage_source = (df_resumes[df_resumes['source'] == 'source']['count'] / total_source) * 100

# Crear el gráfico circular
fig, ax = plt.subplots()
ax.pie([percentage_source_url, percentage_source], labels=['source_url', 'source'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Mostrar el gráfico
st.pyplot(fig)

# Cerrar la conexión a la base de datos
conn.close()
