import mysql.connector
import time
from datetime import date

try:
    conn = mysql.connector.connect(
        host="localhost", 
        user="rohan_jha",
        password="ILoveCoding!@#123",
        database="my_library",
        port=3307
    )
    if conn.is_connected():
         cursor = conn.cursor()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

global today
today = date.today()

def log_in_page():
        print('''
                Library Managment System:
                PRESS:

                        1 ------ Log in
                        2 ------ Sign up
                        3 ------ Find your Member ID
                        4 ------ Quit
                        
                    ''')
    


def main_page():
        print('''
                Library Managment System:
                PRESS:

                        1 ------ Log out
                        2 ------ Check out book
                        3 ------ Return book
                        4 ------ Insert new book
                        5 ------ Delete account
                        6 ------ List of books
                        7 ------ Find your Member ID
                        8 ------ Quit
                    ''')
        

def execute(query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    
    
    
def manipulate_database(sql, val):
    cursor.execute(sql, val)
    conn.commit()
        
    
    
    
def log_in():
        global member_id
        member_id = input('Enter your Member ID: ')
        print('Searching library database...')
        time.sleep(1.25)
        memberid = execute(f'SELECT MemberID FROM members WHERE MemberID = {member_id}')
        if len(memberid) == 0:
            print('Member not found, sign up if you need to.')
        else:
            name = execute(f'SELECT FirstName, LastName FROM members WHERE MemberID = {member_id}')
            print('✅ Successfully logged in, welcome to the library', *name[0],'.')
            time.sleep(1.25)
    
        
    
def log_out():
    print('✅ Logged out successfully.')
    time.sleep(1)
    quit()

    
    
def check_out_book():
    book_id = input('Enter book ID: ')
    book = execute(f'SELECT Title FROM books WHERE BookID = {book_id}')
    sql = "INSERT INTO loans (BookId, MemberID, LoanDate) VALUES (%s, %s, %s)"
    val = (book_id, member_id, today)
    manipulate_database(sql, val)
    print('✅ You have officially checked out:', *book[0])
    time.sleep(2)


    
def return_book():
    loan_id = int(input('Enter the loan_id: '))
    check = execute(f'SELECT Returned FROM loans WHERE LoanID = {loan_id}')
    if check[0] == (1,):
        print('❌ This loan has already been returned.')
        time.sleep(2)
        return
    else:
        sql = "UPDATE loans SET Returned = %s WHERE LoanID = %s"
        val = (1, loan_id)
        manipulate_database(sql, val)
        sql = "UPDATE loans SET ReturnedDate = %s WHERE LoanID = %s"
        val = (today, loan_id)
        manipulate_database(sql, val)
        title = execute(f'SELECT Title FROM books WHERE BookID = (SELECT BookID FROM loans WHERE LoanID = {loan_id})')
        print("✅ Successfully Returned: ",*title[0])
        time.sleep(2)

    
    
def insert_book():
    book_name = input('Enter book name: ')
    author = input('Enter author: ')
    genre = input('Enter genre: ')
    published_year = input('Enter published year: ')
    isbn = int(input('Enter ISBN: '))
    sql = "INSERT INTO books (Title, Author, Genre, PublishedYear, ISBN) VALUES (%s, %s, %s, %s, %s)"
    val = (book_name, author, genre, published_year, isbn)
    manipulate_database(sql, val)
    print(f"✅ Successfully added '{book_name}' into the library system!")
    time.sleep(2)
    
    
    
def delete_account():
    member_id = int(input('Enter your member ID (for deletion): '))
    name = execute(f'SELECT FirstName, LastName FROM members WHERE MemberID = {member_id}')
    confirmation = input('Are you sure you want to delete the account? (press y for yes and n for no): ').lower()
    if confirmation == 'y':
        sql = 'DELETE FROM members WHERE MemberID = %s'
        val = (member_id,)
        manipulate_database(sql, val)
        print("✅ Successfully deleted", *name[0], "'s account")
        time.sleep(2)
    elif confirmation == 'n':
        print('Ok, heading back to the main page...')
        time.sleep(2)
                
    
    
def create_account():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    email = input('Enter email: ')
    phone = input('Enter phone number: ')
    join_date = today
    sql = 'INSERT INTO members (FirstName, LastName, Email, Phone, JoinDate) VALUES (%s, %s, %s, %s, %s)'
    val = (first_name, last_name, email, phone, join_date)
    manipulate_database(sql, val)
    memberid = execute(f'SELECT MemberID FROM members ORDER BY MemberID DESC LIMIT 1')
    print('✅ Successfully created your account! Your member ID is:',*memberid[0])
    time.sleep(2)


def avaliable_books():
     print('Fetching avaliable books...')
     time.sleep(1.5)
     title = execute('SELECT Title FROM books')
     for i in range(len(title)):
          print(*title[i])
          time.sleep(0.2)
     time.sleep(2) 


def find_member_id():
     first_name = input('Enter your first name: ')
     last_name = input('Enter your last name: ')
     memberid = execute(f"SELECT MemberID FROM members WHERE FirstName = '{first_name}' AND LastName = '{last_name}'")
     if len(memberid) > 0:
        print('Your member ID is:',*memberid[0])
     else:
          print('❌ Member ID not found.')
     time.sleep(2)