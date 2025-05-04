def doubler_penny(days):
    amount = 0.01
    for i in range(1, days + 1):
        print(f'Day: {i}: ${amount:.100f}')
        amount *= 2


doubler_penny(200)