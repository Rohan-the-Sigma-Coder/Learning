import mysql.connector
import math


try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="rohan_jha",
        password="ILoveCoding!@#123",
        database="world",
        port=3307
    )
    if conn.is_connected():
        print("✅ Connected to MySQL database successfully!")
        cursor = conn.cursor()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

def execute(query, params=None):
    cursor.execute(query, params or ())
    return cursor.fetchall()

def find_zipcode(user_house_area, user_house_price):
    user_point = (user_house_area, user_house_price)
    rows = execute("SELECT * FROM real_estate_data")
    min_distance = float("inf")
    best_zip = None
    for row in rows:
        point = (int(row[1]), int(row[3]))
        distance = math.dist(user_point, point)
        if distance < min_distance:
            min_distance = distance
            best_zip = row[2] 
    return best_zip

user_house_area = int(input("Enter square feet of house: "))
user_house_price = int(input("Enter price of house: "))
zip_code = find_zipcode(user_house_area, user_house_price)
print(f"Your house is most likely in zip code: {zip_code}")
