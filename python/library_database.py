import mysql.connector
import time
from datetime import date
import Learning.pythonfiles.library_db_functions as library_db_functions
from Learning.pythonfiles.library_db_functions import log_in, log_out, log_in_page, main_page, create_account, delete_account, check_out_book, insert_book, return_book, avaliable_books, find_member_id, conn


try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="rohan_jha",
        password="ILoveCoding!@#123",
        database="my_library",
        port=3307
    )
    
    
    global today
    today = date.today()
    
    
    



    if conn.is_connected():
        print("✅ Connected to MySQL database successfully!")

        cursor = conn.cursor()

        global logged_in
        global choice


        logged_in = False
        
        while True:
            if logged_in == False:
                log_in_page()
            else:
                main_page()
                

            try:
                choice = int(input('Enter choice #️⃣: '))
                if choice > 4 and logged_in == False:
                    print('❌ Please log in or sign up.')
                    time.sleep(1.5)
                elif choice == 1 and logged_in == False:
                    log_in()
                    logged_in = True
                elif choice == 1 and logged_in == True:
                    log_out()
                elif choice == 2 and logged_in == False:
                    create_account()
                elif choice == 7 and logged_in == True:
                    find_member_id()
                elif choice == 3 and logged_in == False:
                    find_member_id()
                elif choice == 4 and logged_in == False:
                    quit()
                elif choice == 8 and logged_in == True:
                    quit()
                elif choice == 2:
                    check_out_book()
                elif choice == 3:
                    return_book()
                elif choice == 4:
                    insert_book()
                elif choice == 5:
                    delete_account()
                elif choice == 6:
                    avaliable_books()
                else:
                    print('❌ Please enter a valid choice.')
                    time.sleep(1.5)    

            except ValueError:
                print('❌ Please enter a valid option.') 
                time.sleep(1.5)      

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")







