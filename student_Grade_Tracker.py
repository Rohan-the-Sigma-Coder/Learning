import datetime
grade_dict = {
    'Rohan': 100,
    'Eshan': 50,
    'Monika': 95,
    'Sachin': 90
}
user_input = input('''Do you want to:

                   a ---- Add entry
                   d ---- Delete entry
                   u ---- Update entry
                   : ''').lower


if user_input == 'a':
    new_name = input('Enter new name: ')
    new_grade = int(input('Enter grade: '))
    grade_dict[f'{new_name}'] = new_grade

print(grade_dict)
# elif user_input == 'u':
    