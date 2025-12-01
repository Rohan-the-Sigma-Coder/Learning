def doubler_penny_1(days):
    amount = 0.01
    for i in range(1, days + 1):
        print(f'Day: {i}: ${amount:.100f}')
        amount *= 2



def doubler_penny_2():
    output = [0.01]
    for i in range(30):
        output.append(output[len(output) - 1] * 2)
    for x in range(0, len(output) - 1):
        print(f'Day {x + 1}: ${output[x]}')



doubler_penny_2()

