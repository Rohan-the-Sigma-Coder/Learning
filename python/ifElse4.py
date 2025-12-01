h = float(input('Enter height in meters: '))
w = float(input('Enter weight in Kg: '))
BMI = w/h
if BMI<14:
    print("Underweight")
elif BMI>=14 and BMI<=24:
    print("Ideal weight")
elif BMI>24 and BMI<=29:
    print("Overweight")
elif BMI>29:
    print("Obese")