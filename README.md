# DSC-510_Introduction-to-programming
DSC-510_Introduction-to-programming
Course Project  
 
Weather Program

For your class project we will be creating an application to interacts with a webservice to obtain data. Your program will use all of the information you’ve learned in the class in order to create a useful application.
The program must prompt the user for their city or zip code and request weather forecast data from OpenWeatherMap.  This program must display the weather information in a READABLE format to the user.

Requirements:

o	Create a header for your program just as you have in the past.
o	Create a Python Application which asks the user for their zip code or city.
o	Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
o	Display the weather forecast in a readable format to the user.
o	Use comments within the application where appropriate to document what the program is doing.
o	Use functions including a main function.
o	Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
o	Validate whether the user entered valid data. If valid data is not presented notify the user.
o	Use the Requests library to request data from the webservice. 
	Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
o	Use Python 3
o	Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether the connection was successful

Deliverables:

o	Final Program in a .py file (Python file)

Program output: 
Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: 1
Please enter the city name: Omaha

Current Weather Conditions For Omaha
Current Temp: 87.1 degrees
High Temp: 89.6 degrees
Low Temp: 86 degrees
Pressure: 1006hPa
Humidity: 29%
Cloud Cover: Minimual Cloud Cover

Would you like to perform another weather lookup? (Y/N)y
Would you like to lookup weather data by US City or zip code? Enter 1 for US City 2 for zip: 2
Please enter the zip code: 68104
Current Weather Conditions For Omaha
Current Temp: 86.67 degrees
High Temp: 87.8 degrees
Low Temp: 86 degrees
Pressure: 1006hPa
Humidity: 29%
Cloud Cover: Minimual Cloud Cover
Would you like to perform another weather lookup? (Y/N)

o	Project Notes:
	This project is a real-world program. I used it as an opportunity to improve my knowledge.
	 I signed up for API Key  by using the above link, which allowed me to get my own API key that I used in the real world program.
	The API key I found is: c05250b637031a772b7adbfe110350c5
	I made a connection to the API using the Requests library.
