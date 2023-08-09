import requests
import geocoder



def get_data(loc):
    
    API_KEY = "d9b20dd2348d0070265e509c7b42d4984428d18d62ac11be2a96db6824f380c6"
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
            print("Error fetching data:", response.status_code)
    else:
        print("Error: Place name not found.")



def get_co(loc):
    data = get_data(loc)
    return data['stations'][0]['CO']

# def get_no2():
#     return data['stations'][0]['NO2']

# def get_ozone():
#     return data['stations'][0]['OZONE']

# def get_pm10():
#     return data['stations'][0]['PM10']

# def get_pm25():
#     return data['stations'][0]['PM25']

# def get_so2():
#     return data['stations'][0]['SO2']

# if __name__ == "__main__":
#     print("CO:", get_co())
#     print("NO2:", get_no2())
#     print("OZONE:", get_ozone())
#     print("PM10:", get_pm10())
#     print("PM25:", get_pm25())
#     print("SO2:", get_so2())
