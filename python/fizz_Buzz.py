import sys
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        print('fizzbuzz')
        sys.exit()
    elif input % 3 == 0:
        print('fizz')
        sys.exit()
    elif input % 5 == 0:
        print('buzz')
        sys.exit()
    else:
        print(input)
        sys.exit()


try:
    input = int(input('Enter a number: '))
except:
    if ValueError:
        print("You're a monkey!")
        sys.exit()
fizz_buzz(input)
