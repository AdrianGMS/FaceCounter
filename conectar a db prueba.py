import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="facecounter",
    user="postgres",
    password="tesis202301"
)

# Crear un cursor para interactuar con la base de datos
cur = conn.cursor()

# Ejecutar una consulta
cur.execute("UPDATE asistencia SET d_asistencia = 'Ausente'")
conn.commit()

# Obtener los resultados de la consulta
#rows = cur.fetchall()

# Cerrar la conexión
cur.close()
conn.close()
