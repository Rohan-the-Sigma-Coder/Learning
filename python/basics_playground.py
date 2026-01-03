import mysql.connector
import requests

try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="rohan_jha",
        password="ILoveCoding!@#123",
        database="stock_market",
        port=3307
    )
    if conn.is_connected():
        print("✅ Connected to MySQL database successfully!")
        cursor = conn.cursor()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

def execute(query):
    cursor.execute(query)
    return cursor.fetchall()

   
def manipulate_database(sql, val):
    cursor.execute(sql, val)
    conn.commit()

def get(url):
    response = requests.get(url)
    return response.json()


# holdings = execute("SELECT total_assets FROM balances WHERE user_id = 1")
# print(holdings[0][0])

# data = get(f"https://financialmodelingprep.com/stable/profile?symbol=AAPL&apikey=zhj0MAKYchz1oswfb27xJ8Lan3kdZ9O7")
# print(data[0])
rows = execute("SELECT quantity FROM holdings WHERE customer_id = 1 AND ticker = 'AAPL'")
print(rows)

