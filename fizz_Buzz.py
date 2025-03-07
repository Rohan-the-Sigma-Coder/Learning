# import sys
# def fizz_buzz(input):
#     if input % 3 == 0 and input % 5 == 0:
#         print('fizzbuzz')
#         sys.exit()
#     elif input % 3 == 0:
#         print('fizz')
#         sys.exit()
#     elif input % 5 == 0:
#         print('buzz')
#         sys.exit()
#     else:
#         print(input)
#         sys.exit()
#
#
# try:
#     input = int(input('Enter a number: '))
# except:
#     if ValueError:
#         print("You're a monkey!")
#         sys.exit()
# fizz_buzz(input)
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