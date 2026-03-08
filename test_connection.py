import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="flight_game"
)

cursor = connection.cursor()

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)