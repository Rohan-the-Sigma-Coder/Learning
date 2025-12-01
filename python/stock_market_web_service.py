import requests

company = input('Enter company abbreviation  (e.g. Amazon ---> AMZN): ')
url = f'https://financialmodelingprep.com/api/v3/profile/{company}?apikey=zhj0MAKYchz1oswfb27xJ8Lan3kdZ9O7'

response = requests.get(url)

if response.status_code == 200:
    original_data = response.json()
    data = original_data[0]
    print(f"Symbol: {data['symbol']}")
    print(f"Company name: {data['companyName']}")
    print(f"Current Price: {data['price']}")
    print(f"Beta: {data['beta']}")
    print(f"Volume Average: {data['volAvg']}")
    print(f"Range: {data['range']}")
    print(f"Market Cap: {data['mktCap']}")
    print(f"CEO: {data['ceo']}")
    print(f"Full Time Employees: {data['fullTimeEmployees']}")
else:
    print(f'Something went wrong: {response.status_code}')