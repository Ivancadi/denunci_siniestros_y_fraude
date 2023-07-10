import mysql.connector

configuracion = {
  'user': 'root',
  'password': 'Aprender2023',
  'host': 'localhost',
  'database': 'R5',
  'raise_on_warnings': True
}

conexion = mysql.connector.connect(**configuracion)

cursor = conexion.cursor()

# Ejecuta la consulta
query = "SELECT * FROM fraudes WHERE DayOfWeekClaimed != '0'"
cursor.execute(query)

# Recupera los resultados de la consulta
results = cursor.fetchall()

# Imprime los resultados
for row in results:
    print(row)

cursor.close()
conexion.close()
