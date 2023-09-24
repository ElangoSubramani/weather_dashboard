import requests
import geocoder



def get_data(loc):
    
    API_KEY = "14842c6440662011587a3c43bd131abc1d35d1d65af9878d922d87ecaeb4503e"
    place_name = str(loc)

    location = geocoder.osm(place_name)
    if location.ok:
        lat = location.latlng[0]
        lng = location.latlng[1]

        url = f"https://api.ambeedata.com/latest/by-lat-lng?lat={lat}&lng={lng}"

        headers = {
            "x-api-key": API_KEY,
            "Content-type": "application/json",
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None         # print("Error fetching data:", response.status_code)
    else:
        return None



def get_AQI(loc):
    try:
        data = get_data(loc)
        return data['stations'][0]['AQI']
    except:
        return None

def get_no2(loc):
    try:
        data = get_data(loc)
        return data['stations'][0]['NO2']
    except:
        return None

def get_ozone(loc):
    try:
        data = get_data(loc)
        return data['stations'][0]['OZONE']
    except:
        return None

def get_pm10(loc):
    try:
        data = get_data(loc)
        return data['stations'][0]['PM10']
    except:
        return None

def get_pm25(loc):
    try:
        data = get_data(loc)
        return data['stations'][0]['PM25']
    except:
        return None

def get_so2(loc):
    try:
        data = get_data(loc)
        return data['stations'][0]['SO2']
    except:
        return None

# if __name__ == "__main__":
#     loc="chennai"
#     print("CO:", get_co(loc))
#     print("NO2:", get_no2())
#     print("OZONE:", get_ozone())
#     print("PM10:", get_pm10())
#     print("PM25:", get_pm25())
#     print("SO2:", get_so2())
