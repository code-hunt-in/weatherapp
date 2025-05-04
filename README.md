# weatherapp
Weather Dashboard (No API Key Required)
=======================================

This is a simple Flask-based weather dashboard where users can enter a city name and get the current weather conditions using free APIs (OpenStreetMap + Open-Meteo). No API key is needed!

---------------------------------------
Features
---------------------------------------
- ✅ Live weather data using Open-Meteo API
- ✅ Free location lookup via OpenStreetMap Nominatim
- ✅ No API key or account required
- ✅ Clean and responsive UI (HTML, CSS, JavaScript)
- ✅ Built using Python and Flask

---------------------------------------
Project Structure
---------------------------------------

weather-dashboard/
├── app.py                -> Main Flask backend
├── templates/
│   └── index.html        -> Frontend (Jinja2 template)
├── static/
│   └── style.css         -> CSS for styling
└── README.txt            -> This file

---------------------------------------
How to Run
---------------------------------------

1. Clone the Repository
-----------------------
git clone https://github.com/code-hunt-in/weatherapp.git
cd weatherapp

2. Install Dependencies
-----------------------
Make sure Python 3 and pip are installed.

pip install flask requests

3. Run the App
--------------
python app.py

4. Open in Browser
------------------
Visit: http://127.0.0.1:5000

---------------------------------------
How It Works
---------------------------------------

1. User enters a city name
2. Flask calls OpenStreetMap Nominatim API to get latitude and longitude
3. It then fetches weather using Open-Meteo API
4. Weather info (temperature, windspeed, condition) is displayed

---------------------------------------
APIs Used
---------------------------------------
- OpenStreetMap Nominatim (Geocoding)
- Open-Meteo Weather API

---------------------------------------
Future Ideas
---------------------------------------
- Add weather icons and readable descriptions
- Add multi-day forecast
- Integrate maps for location visualization
- Convert to mobile app

---------------------------------------
License
---------------------------------------
MIT License — Free to use and modify

---------------------------------------
Author
---------------------------------------
Aishwary Pandore
