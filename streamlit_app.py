import streamlit as st
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname="tg",
    user="analyst",
    password="n5NwBhOz9kEc",
    host="ep-soft-king-a5iqrjku.us-east-2.aws.neon.tech"
)

# Consulta SQL para obtener la cantidad de usuarios
query_users_count = "SELECT COUNT(DISTINCT user_id) FROM users_tokens;"

# Consulta SQL para obtener la cantidad de usuarios creados por fecha
query_users_by_date = "SELECT date_created, COUNT(DISTINCT anon_user_id) AS user_count FROM users GROUP BY date_created;"

# Consulta SQL para obtener la cantidad de source_url vs source
query_source_counts = "SELECT COUNT(DISTINCT source_url) AS url_count, COUNT(DISTINCT source) AS source_count FROM resumes;"

# Ejecutar consultas SQL y obtener resultados
cur = conn.cursor()
cur.execute(query_users_count)
user_count = cur.fetchone()[0]

cur.execute(query_users_by_date)
users_by_date = cur.fetchall()
users_by_date_df = pd.DataFrame(users_by_date, columns=['Date', 'User Count'])
users_by_date_df['Date'] = pd.to_datetime(users_by_date_df['Date'])

cur.execute(query_source_counts)
source_counts = cur.fetchone()
url_count = source_counts[0]
source_count = source_counts[1]

# Cerrar conexión
cur.close()
conn.close()

# Crear el dashboard con Streamlit
st.title('Dashboard PostgreSQL')

# Mostrar la cantidad total de usuarios
st.subheader('Cantidad total de usuarios:')
st.write(user_count)

# Gráfico de cantidad de usuarios creados por fecha
st.subheader('Cantidad de usuarios creados por fecha:')
st.line_chart(users_by_date_df.set_index('Date'))

# Porcentaje de source_url vs source
st.subheader('Porcentaje de source_url vs source:')
st.write(f'Porcentaje de source_url: {url_count / (url_count + source_count) * 100:.2f}%')
st.write(f'Porcentaje de source: {source_count / (url_count + source_count) * 100:.2f}%')
