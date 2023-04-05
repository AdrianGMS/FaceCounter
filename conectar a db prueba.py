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
cur.execute("SELECT * FROM asistencia")

# Obtener los resultados de la consulta
rows = cur.fetchall()

for row in rows:
    print(row)
# Cerrar la conexión
cur.close()
conn.close()
