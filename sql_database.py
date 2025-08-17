import mysql.connector

try:
    # Establish the connection
    conn = mysql.connector.connect(
        host="localhost",  # Or the IP address/hostname of your MySQL server
        user="rohan_jha",
        password="ILoveCoding!@#123",
        database="my_library",
        port=3307
    )

    if conn.is_connected():
        print("Connected to MySQL database successfully!")

        cursor = conn.cursor()
        author = input("Enter the name of an author, and I'll show you their books (full name): ")
        cursor.execute(f"SELECT Title FROM books WHERE Author = '{author}'")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        

except mysql.connector.Error as err:
    print(f"Error: {err}")







