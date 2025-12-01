import re
def check_password_strength(password):
    if len(password) < 8:
        print('Invalid password')
        quit()
    elif not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    elif not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    elif not re.search(r'[0-9]', password):
        return "Password must contain at least one number."
    elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    else:
        return "Password meets requirements."
    

password = input('Enter password: ')
print(check_password_strength(password))
  
