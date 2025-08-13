# Weather App 🌤️

A graphical weather application built with Python and Tkinter that allows users to input a city and get detailed weather data, including temperature, description, wind speed, and weather icons, fetched from the OpenWeatherMap API. The application provides a simple, user-friendly interface for users to quickly check the weather in any location.

## Features

- 🌍 Search for Weather by City: Enter any city name to get real-time weather information.
- 🌡️ Current Weather Conditions: Display temperature, weather description, and wind speed.
- 🖼️ Weather Icons: Displays weather-related icons like sunny, cloudy, rainy, etc.
- 📏 User-Friendly Design: Clean and intuitive interface using Tkinter, with enhanced styling for a pleasant user experience.

## Tech Stack

- Language: Python 🐍
- Libraries:
  - Tkinter: For creating the graphical user interface (GUI).
  - requests: To fetch weather data from the OpenWeatherMap API.
  - Pillow (PIL): For displaying weather icons.
  - io: For handling binary data of images.
- API: [OpenWeatherMap](https://openweathermap.org/) for real-time weather data.


## Prerequisites

To run this project locally, you need to have the following installed:

1. Python 3.x - [Download Python](https://www.python.org/downloads/)
2. Pillow (PIL) for handling images:  
   Install it by running:
  ```bash
   pip install pillow
```
   
3. Requests for fetching data from the weather API:  
   Install it by running:
  ```bash
   pip install requests
```
   
## Installation

1. Clone the repository:
  ```bash
git clone https://github.com/sujal-ec/OIBSIP_weather_app.git
cd OIBSIP_weather_app.git
   ```


3. Install the dependencies:
  
```bash
   pip install -r requirements.txt
   ```
   
4. Obtain your OpenWeatherMap API key by signing up on their website:  
   [OpenWeatherMap API Signup](https://home.openweathermap.org/users/sign_up)

5. Replace 'YOUR_API_KEY' in the weather_app.py file with your actual OpenWeatherMap API key:
  
```python
   API_KEY = '7a7536317011245bf9fd3274b32f42bc'
   ```

6. Run the app:

   ```bash
   python weather_app.py
   ```
## Usage

1. Launch the application by running the weather_app.py script.
2. Enter the name of the city for which you want to get the weather.
3. Click on the Get Weather button to display the weather information including temperature, description, wind speed, and a corresponding weather icon.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you find a bug or have an idea for improvement.

