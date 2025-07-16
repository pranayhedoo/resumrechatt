# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid=d0d72530db030d22671e2fc8f167ed37

# d0d72530db030d22671e2fc8f167ed37

import requests

# Replace with your actual API key
API_KEY = 'your_api_key_here'
city = 'London'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    data = response.json()  # Convert JSON response to Python dict

    temperature = data['main']['temp']   # Access the current temp. from the json

    weather = data['weather'][0]['description']   # Access the data from list

    print(f"The temperature in {city} is {temperature}°C with {weather}.")
else:
    print(f"Failed to retrieve data: {response.status_code}")

# import requests

# # Public Cat Facts API URL
# url = "https://catfact.ninja/fact"

# # Send GET request
# response = requests.get(url)

# # Check if request was successful
# if response.status_code == 200:
#     data = response.json()  # Convert JSON response to Python dictionary
#     fact = data['fact']
#     print("Random Cat Fact:", fact)
# else:
#     print("Failed to retrieve cat fact:", response.status_code)
 
def divide_numbers(a, b):
    try:
        if b == 0:
            return "Cannot divide by zero."
        elif a == 0:
            return "Numerator is zero. Result is 0."
        else:
            result = a / b
            return f"Result: {result}"
    except TypeError:
        return "Error: Please enter numbers only."
    finally:
        print("Operation attempted.")
