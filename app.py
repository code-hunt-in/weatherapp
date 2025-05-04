from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    headers = {
        "User-Agent": "WeatherDashboardApp/1.0 (aishwary.pandore@somaiya.edu)"
    }
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return lat, lon
    except Exception as e:
        print("Error decoding JSON:", e)
    return None, None

def get_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url).json()
    return response.get('current_weather', {})

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    city = ''
    if request.method == 'POST':
        city = request.form['city']
        lat, lon = get_coordinates(city)
        if lat and lon:
            weather = get_weather(lat, lon)
    return render_template('index.html', weather=weather, city=city)

if __name__ == '__main__':
    app.run(debug=True)
