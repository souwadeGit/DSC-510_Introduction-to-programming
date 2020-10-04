import requests
from pprint import pprint

# Global Variables
# Note that there are restrictions on the "Free API"  Make sure that you don't submit too many requests

apiKey = "d5751b1a9e2e4b2b8c7983646072da8b"
url = "http://api.openweathermap.org/data/2.5/weather"
headers = {
    'cache-control': "no-cache",
}


# This method will do a weather lookup by city
# This method takes the city as a parameter
def retrieveWeatherByCity(city):
    querystring = {"q": city + ",us", "units": "imperial", "APPID": apiKey}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except requests.exceptions.RequestException as e:
        print(e)

    parseWeather(response)


# This method will do a weather lookup by zip
# This method takes the zipCode as a parameter
def retrieveWeatherByZip(zipCode):
    querystring = {"zip": zipCode + ",us", "units": "imperial", "APPID": apiKey}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except requests.exceptions.RequestException as e:
        print(e)

    # print(response.url)
    # print(response.text)

    parseWeather(response)


# This method will parse the weather data and then present that weather data to the user
# This method takes the response as a parameter
def parseWeather(response):
    weatherJSON = response.json()

    # pprint(weatherJSON) This is a great troubleshooting line which can be quickly enabled to see your JSON
    pressure = weatherJSON['main']['pressure']
    temp = weatherJSON['main']['temp']
    maxTemp = weatherJSON['main']['temp_max']
    minTemp = weatherJSON['main']['temp_min']
    humidity = weatherJSON['main']['humidity']
    clouds = weatherJSON['clouds']['all']

    if (clouds > 75):
        cloudiness = "Full Cloud Cover"
    elif (clouds > 50 and clouds < 75):
        cloudiness = "Partial Cloud Cover"
    else:
        cloudiness = "Minimual Cloud Cover"
    print("\nCurrent Weather Conditions For " + weatherJSON['name'])
    print("Current Temp: " + str(temp) + " degrees")
    print("High Temp: " + str(maxTemp) + " degrees")
    print("Low Temp: " + str(minTemp) + " degrees")
    print("Pressure: " + str(pressure) + "hPa")
    print("Humidity: " + str(humidity) + "%")
    print("Cloud Cover: " + cloudiness)


# This is the main method
# This method will prompt the user to make a selection between doing a weather lookup based upon city or zipcode
# The main method will then call a method to do the weather lookup based upon whether the user entered a city or zip
def main():
    runApp = True
    # The program should allow the user to run it multiple times.  This is one way to do that.
    while runApp:
        lookupType = input(
            "\nWould you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: ")

        if (lookupType == "1"):
            city = input("Please enter the city name: ")
            retrieveWeatherByCity(city)
        elif (lookupType == "2"):
            zipCode = input("Please enter the zip code: ")
            retrieveWeatherByZip(zipCode)
        else:
            print("Enter a valid option.  Please enter 1 to lookup by city.  Enter 2 to lookup by zip code")
        runApp = input("\nWould you like to perform another weather lookup? (Y/N)").lower()
        if runApp in 'n':
            break


if __name__ == "__main__":
    main()