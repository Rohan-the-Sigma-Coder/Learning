import requests
from datetime import datetime as date
import mysql.connector
import time
import os
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import HumanMessage
global now
global change
now = date.now()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # Chat-compatible model
    temperature=0.7,
    max_new_tokens=200
)
chat_llm = ChatHuggingFace(llm=llm)

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

def execute(query, params=None):
    cursor.execute(query, params or ())
    return cursor.fetchall()

   
def manipulate_database(sql, val):
    cursor.execute(sql, val)
    conn.commit()

def get(url):
    response = requests.get(url)
    return response.json()

def order(symbol, quantity):
    data = get(f"https://financialmodelingprep.com/stable/profile?symbol={symbol}&apikey=zhj0MAKYchz1oswfb27xJ8Lan3kdZ9O7")
    if not data:
        print("Invalid symbol")
        return
    data = data[0]
    price = float(data['price'])
    amount = price * quantity
    company = data['companyName']
    return amount, company

def buy_stock(user_id):
    symbol = input("Symbol: ")
    quantity = int(input("Quantity (shares): "))
    if quantity == 0:
        return
    result = order(symbol, quantity)
    if result is None:
        return
    amount, company = result
    unit_price = get(f"https://financialmodelingprep.com/stable/profile?symbol={symbol}&apikey=zhj0MAKYchz1oswfb27xJ8Lan3kdZ9O7")
    unit_price = unit_price[0]
    unit_price = float(unit_price['price'])
    rows = execute("SELECT balance FROM balances WHERE user_id = %s", (user_id,))
    if not rows:
        print('No balance row for this user')
        return
    balance = float(rows[0][0])
    if amount > balance:
        print("Not enough funds.")
        return
    balance -= amount
    manipulate_database(
        "UPDATE balances SET balance = %s "
        "WHERE user_id = %s",
        (balance, user_id),
    )
    manipulate_database("INSERT INTO holdings (customer_id, ticker, quantity, unit_price) VALUES (%s, %s, %s, %s)",  
                        (user_id, symbol, quantity, unit_price,))
    manipulate_database("INSERT INTO stock_orders (user_id, timestamp, order_type, ticker, shares_quantity, price) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (user_id, now, "buy", symbol, quantity, unit_price))
    

def sell_stock(user_id):
    symbol = input("Symbol: ")
    quantity = int(input("Quantity (shares): "))
    result = order(symbol, quantity)
    if result is None:
        return
    amount, company = result
    unit_price = get(f"https://financialmodelingprep.com/stable/profile?symbol={symbol}&apikey=zhj0MAKYchz1oswfb27xJ8Lan3kdZ9O7")
    unit_price = unit_price[0]
    unit_price = float(unit_price['price'])
    rows = execute("SELECT balance FROM balances WHERE user_id = %s", (user_id,))
    if not rows:
        print('No balance row for this user')
        return
    balance = int(rows[0][0])
    balance += amount
    manipulate_database(
        "UPDATE balances SET balance = %s WHERE user_id = %s",
        (balance, user_id),
    )
    rows = execute(
    "SELECT quantity FROM holdings WHERE customer_id = %s AND ticker = %s",
    (user_id, symbol),
)   
    if not rows:
        print("You do not hold this stock.")
        return
    if quantity == 0:
        return
    current_quantity = rows[0][0]
    if quantity > current_quantity:
        print("Cannot sell more than you hold.")
        return
    if current_quantity - quantity == 0:
        manipulate_database("DELETE FROM holdings WHERE customer_id = %s AND ticker = %s", (user_id, symbol,))
    manipulate_database("UPDATE holdings SET quantity = %s, unit_price = %s WHERE customer_id = %s AND ticker = %s", (current_quantity - quantity, unit_price, user_id, symbol))
    manipulate_database("INSERT INTO stock_orders (user_id, timestamp, order_type, ticker, shares_quantity, price) VALUES (%s, %s, %s, %s, %s, %s)", 
                        (user_id, now, "sell", symbol, quantity, unit_price))


signed_in = False

def log_in_page():
    print("""Welcome to the Investing App! This is a stock market simulation app designed to help people learn about the investing world.
      1 - Sign in
      2 - Sign up
      """)

def main_page():
    print("""Welcome to the main screen, here you have a variety of different option to choose from:
          1 - Buy
          2 - Sell
          3 - Total change
          4 - Balances
          5 - Purchase
          6 - Ai Assistance
          7 - Log out
          8 - Delete Account""")

while True:    
    if signed_in == False:
        log_in_page()
        user_input = int(input("Choice: "))
        if user_input == 1:
            user_id = input("Enter user id: ")
            rows = execute("SELECT id FROM users WHERE id = %s", (user_id,))
            if not rows:
                print("User not found")
            else:
                user_id = rows[0][0]
                user_name = execute("SELECT first_name, last_name FROM users WHERE id = %s", (user_id,))
                firstname, lastname = user_name[0]
                time.sleep(0.75)
                print(f"Welcome to the investing app {firstname} {lastname}!")
                time.sleep(1)
                signed_in = True

        elif user_input == 2:
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number (###-###-####): ")
            manipulate_database("INSERT INTO users (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, phone,))
            user_ID = execute("SELECT id FROM users WHERE phone = %s", (phone,))
            user_ID = user_ID[0][0]
            manipulate_database("INSERT INTO balances (user_id, balance, total_change, total_assets) VALUES (%s, %s, %s, %s)", (user_ID, 1000000, 0, 1000000,))


    else:
        main_page()
        user_input = int(input("Choice: "))
            
        if user_input == 1:
            buy_stock(user_id)

        elif user_input == 2:
            sell_stock(user_id)

        elif user_input == 3:
            company_list = []
            add_list = []
            holdings = execute("SELECT ticker FROM holdings WHERE customer_id = %s", (user_id,))
            for row in holdings:
                company_list.append(row[0])
            change = 0
            for i in range(len(company_list)):
                price_data = get(f"https://financialmodelingprep.com/stable/profile?symbol={company_list[i]}&apikey=zhj0MAKYchz1oswfb27xJ8Lan3kdZ9O7")
                price = float(price_data[0]["price"])
                stock_quantity = execute(
                    "SELECT quantity FROM holdings WHERE customer_id = %s AND ticker = %s",
                    (user_id, company_list[i]),
                )
                result = sum(hold[0] for hold in stock_quantity)
                add_list.append(result * price)

            total_sum = sum(add_list)
            total_assets = float(execute("SELECT total_assets FROM balances WHERE user_id = %s", (user_id,))[0][0])
            currentbalance = float(execute("SELECT balance FROM balances WHERE user_id = %s", (user_id,))[0][0])
            change = (currentbalance + total_sum) - total_assets
            manipulate_database("UPDATE balances SET total_change = %s WHERE user_id = %s", (change, user_id))
            rows = execute("SELECT total_change FROM balances WHERE user_id = %s", (user_id,))
            if rows:
                total_change = rows[0][0]
                print(f"Total gain/loss: ${total_change}")
            else:
                print("No balance row for this user.")
            time.sleep(1)


        elif user_input == 4:
            balance = execute("SELECT balance FROM balances WHERE user_id = %s", (user_id,)) # type: ignore
            balance = balance[0][0]
            total_assets = execute("SELECT total_assets FROM balances WHERE user_id = %s", (user_id,)) # type: ignore
            total_assets = total_assets[0][0]
            print(f"""
                Current Balance: ${balance}
                Total Assets: ${total_assets}
                """)
            time.sleep(4)

        elif user_input == 5:
            bought_item = input("What do you want to buy (anything, specificity gives more accurate price): ")
            amount = int(input("How much or many of that thing: "))
            cost = chat_llm.invoke([HumanMessage(content=f"How much would {amount} {bought_item} cost? Give me only the price and nothing else. NO DOLLAR SIGN, JUST NUMBER.")])
            cost = cost.content
            print(f"Cost: ${cost}")
            confirmation = input("Are you sure you want to buy it? (Y for yes, N for no): ").upper()
            if confirmation == 'Y':
                manipulate_database("INSERT INTO purchases (user_id, item, unit_price, quantity) VALUES (%s, %s, %s, %s)", (user_id, bought_item, int(cost), amount,))
                print("Puchasing...")
                time.sleep(1)
            current_balance = execute("SELECT balance FROM balances WHERE user_id = %s", (user_id,))
            current_balance = current_balance[0][0]                
            manipulate_database("UPDATE balances SET balance = %s WHERE user_id = %s", (current_balance - int(cost), user_id,))

        elif user_input == 6:
            while True:
                prompt = input("What's on your mind (type 'quit' to exit): ")
                if prompt.lower() == "quit":
                    break

                ai_msg = chat_llm.invoke([
                    HumanMessage(content=f"{prompt} (Only 200 words)")
                ])
                print(f"AI: {ai_msg.content}")


        elif user_input == 7:
            signed_in = False

        elif user_input == 8:
            confirmation = input("Are you sure you want to delete your account? (Y for yes, N for no): ").upper()
            if confirmation == "Y":
                manipulate_database("DELETE FROM users WHERE id = %s", (user_id,))
            elif confirmation == "N":
                main_page()








