full_name = input(("What is the patient's full name?"))
age = input(("What is the patient's age?"))
is_new = input(("Is the patient new? (Answer Yes or No)"))
if is_new == 'Yes':
    dec = 'is'
if is_new == 'No':
    dec = 'is not'
print('His full name is',full_name, 'and his age is',age,'years old. He', dec, 'a new patient.')