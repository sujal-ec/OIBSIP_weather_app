import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io

API_KEY = '7a7536317011245bf9fd3274b32f42bc'

# Function to fetch weather data
def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(base_url)
    return response.json()

# Function to update weather information
def display_weather():
    city = city_entry.get()
    weather_data = get_weather(city)

    if weather_data.get("cod") != 200:
        messagebox.showerror("Error", "City not found or invalid API key.")
        return

    # Extract weather information
    city_name = weather_data["name"]
    temp = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]
    icon_code = weather_data["weather"][0]["icon"]

    # Update labels in the GUI
    city_label.config(text=f"Weather in {city_name}")
    temp_label.config(text=f"Temperature: {temp}°C")
    desc_label.config(text=f"Description: {description.capitalize()}")
    wind_label.config(text=f"Wind Speed: {wind_speed} m/s")

    # Fetch and display weather icon
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_response = requests.get(icon_url)
    img_data = icon_response.content
    icon_img = Image.open(io.BytesIO(img_data))
    icon_img = icon_img.resize((100, 100), Image.Resampling.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_img)
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo  

app = tk.Tk()
app.title("Weather App")
app.geometry("400x500")
app.config(bg="#add8e6") 


city_entry = tk.Entry(app, font=("Arial", 16), width=20, bd=3, relief="groove")
city_entry.pack(pady=20)

get_weather_button = tk.Button(app, text="Get Weather", font=("Arial", 14), command=display_weather, bg="#4682b4", fg="white", bd=2, relief="raised")
get_weather_button.pack(pady=10)

city_label = tk.Label(app, text="Weather Info", font=("Arial", 18, "bold"), bg="#add8e6", fg="#333")
city_label.pack(pady=10)

temp_label = tk.Label(app, text="Temperature: ", font=("Arial", 16), bg="#add8e6", fg="#333")
temp_label.pack()

desc_label = tk.Label(app, text="Description: ", font=("Arial", 16), bg="#add8e6", fg="#333")
desc_label.pack()

wind_label = tk.Label(app, text="Wind Speed: ", font=("Arial", 16), bg="#add8e6", fg="#333")
wind_label.pack()

icon_label = tk.Label(app, bg="#add8e6")
icon_label.pack(pady=20)

app.mainloop()
