import streamlit as st
import pandas as pd
import psycopg2
import matplotlib.pyplot as plt
import seaborn as sns

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

# Mostrar el resultado en un gráfico
st.title('Cantidad Total de user_id')
st.write(f"La cantidad total de user_id es: {df['total_users'][0]}")


# Consulta SQL para obtener los datos
query2 = "SELECT source, source_url, COUNT(id) as count FROM resumes GROUP BY source, source_url"

# Ejecutar la consulta y obtener los datos en un DataFrame
df = pd.read_sql(query2, conn)

# Cerrar la conexión a la base de datos
conn.close()

# Calcular porcentajes
df['total'] = df.groupby('source')['count'].transform('sum')
df['percentage'] = (df['count'] / df['total']) * 100

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar
for i, (source, group) in enumerate(df.groupby('source')):
    ax.barh(group['source_url'], group['percentage'], label=source)

# Personalizar el gráfico
ax.set_xlabel('Porcentaje (%)')
ax.set_ylabel('source_url')
ax.set_title('Diferencia de source_url vs source en porcentaje en relación a id')
ax.legend()

# Mostrar el gráfico
st.pyplot(fig)
