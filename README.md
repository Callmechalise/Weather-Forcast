**Weather App:**

Weather App is a simple graphical user interface (GUI) application built using Python's Tkinter library that allows users to check the current weather conditions of any city. The app uses the OpenWeatherMap API to fetch weather data and displays it along with the local time of the queried city.

**Features:**

Search for weather conditions by city name.
Displays current temperature, weather condition, wind speed, humidity, pressure, and a brief description.
Shows local time for the specified city.
User-friendly interface with image icons.

**Requirements**

Before running the application, ensure you have the following Python packages installed:
tkinter (usually included with Python)
requests
geopy
timezonefinder
pytz
PIL (Pillow)
You can install the required packages using pip:

**bash**
Copy code**
**pip install requests geopy timezonefinder pytz Pillow****

Getting Started
Clone the repository or download the code.

Set up your OpenWeatherMap API Key:

Sign up at OpenWeatherMap to obtain an API key.
Replace the placeholder in the code with your actual API key:
python
Copy code
api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=YOUR_API_KEY"
Run the application:

Ensure that you have the required image files (search.png, search_icon.png, Logo.png, box.png) in the same directory as the script.
Execute the script using Python:
bash
Copy code
python weather_app.py

**Usage**
Launch the application.
Enter a city name in the search box and click the search icon.
The current weather information and local time will be displayed.

**Screenshots**:
![Screenshot (33)](https://github.com/user-attachments/assets/acd0c1f9-12e0-4e6a-b95c-0a0b1356df59)
![Screenshot (32)](https://github.com/user-attachments/assets/db19c9de-94a1-4d1b-86a9-e6cdc1682a43)
![Screenshot (34)](https://github.com/user-attachments/assets/51e84f47-f5f9-4bf4-9812-0bc94e6e88ed)


**Troubleshooting**

If you encounter an error while fetching weather data, ensure that the city name is spelled correctly.
Make sure your internet connection is active, as the app needs to access the OpenWeatherMap API.
License
This project is licensed under the MIT License - see the LICENSE file for details.

**Acknowledgements**:

OpenWeatherMap for the weather API.
Geopy for geocoding.
Pillow for image handling.


Some gui items is taken from
https://www.youtube.com/@parvatcomputertechnology
Checkout him

There is some gui error in app too 
