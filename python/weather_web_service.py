import requests

def celsius_to_farenheight(c):
    return (c * 9/5) + 32



api_key = 'c6d3762cc0c705a10a93a3ef3bed9ec9'
city = input('Enter a city: ')
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"City: {data['name']}")
    print(f"Weather: {data['weather'][0]['description']}")
    celsius = data['main']['temp']
    farenheight = int(celsius_to_farenheight(celsius))
    print(f"Temperature: {farenheight}°F")

else:
    print(f"Failed to get weather data: {response.status_code}")

