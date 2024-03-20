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

# Crear el gráfico
#plt.figure(figsize=(8, 6))
#sns.barplot(x=df.index, y='total_users', data=df)
#plt.xlabel('Usuarios')
#plt.ylabel('Cantidad')
#plt.title('Cantidad Total de user_id')
#st.pyplot(plt.gcf())
st.info(f"La cantidad total de usuarios es: {df['total_users'][0]}")
from streamlit.components.v1 import html

html("""
<div style="font-size: 36px; text-align: center;">
  <span id="count" style="color: blue;"></span>
</div>

<script>
var count = 0;
var target = {0}; // Aquí debes colocar el valor de la cantidad total de usuarios

setInterval(function() {{
  if (count < target) {{
    count++;
    document.getElementById('count').innerHTML = count;
  }}
}}, 50);
</script>
""".format(df['total_users'][0]))
aaaaaa