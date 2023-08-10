import requests
def get_weather_data(loc):
    W_API_KEY = 'd853b076ffa7f29a3a0992fe98fba4b6'
    LOCATION = loc
    BASE_URL = 'http://api.weatherstack.com/current'
    url = f'{BASE_URL}?access_key={W_API_KEY}&query={LOCATION}'
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            return None
    except Exception as e:
        print('An error occurred:', str(e))
    return None


def get_country(loc):
    try:
        data= get_weather_data(loc)
        return data['location']['country']
    except:
        return None

def get_temperature(loc):
    try:
        data= get_weather_data(loc)
        return data['current']['temperature']
    except:
        return None



def get_weather_description(loc):
    try:
        data= get_weather_data(loc)
        return data['current']['weather_descriptions'][0]
    except:
        return None

def get_humidity(loc):
    try:
        data= get_weather_data(loc)
        return data['current']['humidity']
    except:
        return None

def get_wind_speed(loc):
    try:
        data= get_weather_data(loc)
        return data['current']['wind_speed']
    except:
        None

# if __name__ == "__main__":
#     loc="chennai"
#     weather_data = get_weather_data(loc)
#     if weather_data:
#         location = get_location(weather_data)
#         country = get_country(weather_data)
#         temperature = get_temperature(weather_data)
#         weather_description = get_weather_description(weather_data)
#         humidity = get_humidity(weather_data)
#         wind_speed = get_wind_speed(weather_data)

#         print(f'Weather in {location}, {country}:')
#         print(f'Description: {weather_description}')
#         print(f'Temperature: {temperature}°C')
#         print(f'Humidity: {humidity}%')
#         print(f'Wind Speed: {wind_speed} km/h')
