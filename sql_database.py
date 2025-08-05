import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Welcome!23'
)

if connection.is_connected():
    db_info = connection.get_server_info()
    print('Connected to mySQL server:', db_info)
    connection.close()