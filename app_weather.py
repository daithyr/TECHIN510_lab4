import os
import streamlit as st
import requests
from datetime import datetime
from geopy.geocoders import Nominatim
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Meteomatics API credentials
METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")

# Define the weather emojis dictionary
weather_emojis = {
    0: "❓",  # Unknown
    1: "☀️",  # Clear sky
    2: "🌤️",  # Mostly clear sky
    3: "⛅",  # Partly cloudy
    4: "🌥️",  # Mostly cloudy
    5: "☁️",  # Overcast
    6: "🌧️",  # Light rain
    7: "🌦️",  # Rain showers
    8: "🌧️",  # Rain
    9: "🌨️",  # Snow
    10: "❄️",  # Snow showers
    11: "🌩️",  # Thunderstorm
    12: "🌫️",  # Fog
}

# Function to get city coordinates
def get_city_coordinates(city):
    geolocator = Nominatim(user_agent="weather_app")
    try:
        location = geolocator.geocode(city, timeout=5)
        if location:
            return location.latitude, location.longitude
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching city coordinates: {e}")
        return None

# Function to get weather data
def get_weather_data(latitude, longitude):
    base_url = "https://api.meteomatics.com"
    now = datetime.utcnow()
    parameters = "t_2m:C,weather_symbol_1h:idx"
    time_range = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    url = f"{base_url}/{time_range}/{parameters}/{latitude},{longitude}/json"
    
    try:
        response = requests.get(url, auth=(METEOMATICS_USERNAME, METEOMATICS_PASSWORD))
        if response.status_code == 200:
            return response.json()
        else:
            st.warning("Failed to retrieve weather data.")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {e}")
        return None

# Function to display weather information
def display_weather_info(city):
    coordinates = get_city_coordinates(city)
    if coordinates:
        latitude, longitude = coordinates
        weather_data = get_weather_data(latitude, longitude)
        if weather_data:
            st.subheader(f"Weather Forecast for {city}")

            # Current temperature and general weather state
            current_temp = weather_data['data'][0]['coordinates'][0]['dates'][0]['value'] if weather_data['data'] and weather_data['data'][0]['coordinates'] else "N/A"
            current_weather_state = weather_data['data'][1]['coordinates'][0]['dates'][0]['value'] if weather_data['data'] and weather_data['data'][1]['coordinates'] else 0
            current_emoji = weather_emojis.get(current_weather_state, "❓")
            st.write(f"Current Temperature: {current_temp}°C {current_emoji}")
        else:
            st.warning("Failed to retrieve weather data.")
    else:
        st.warning("City not found. Please enter a valid city.")

# Streamlit app layout
def main():
    st.title("Weather Lookup App")
    st.write("Enter a city to get the current weather information.")

    city = st.text_input("Enter city name")
    if st.button("Get Weather"):
        if city:
            display_weather_info(city)
        else:
            st.warning("Please enter a city name.")

if __name__ == "__main__":
    main()
