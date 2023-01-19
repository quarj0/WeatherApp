"""
Author: Owusu Ansah
Application name: Weather update
app version: 1.2
"""


# importing required libraries
from tkinter import *
from datetime import *
from tkinter import messagebox
import pytz
import requests
from geopy.geocoders import *
from timezonefinder import *


# initializing tkinter
root = Tk()
root.title("Weather Update")

# This gives the size of the application
root.geometry("720x480+300+200")
root.resizable(False, False)

# search bar
search_bar = PhotoImage(file="search.png")
search_image = Label(image=search_bar)
search_image.place(x=20, y=20)

# text field
textfield = Entry(
    root,
    justify="center",
    width=17,
    font=("Times New Roman", 25, "bold"),
    background="#404040",
    foreground="white",
)
textfield.place(x=30, y=40)
textfield.focus()
box = PhotoImage(file="box.png")
box_image = Label(image=box)
box_image.place(x=38, y=375)


# defining my weather


def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)

        tzm = TimezoneFinder()
        rst = tzm.timezone_at(lng=location.longitude, lat=location.latitude)
        hme = pytz.timezone(rst)
        utc = datetime.now(hme)
        time_now = utc.strftime("%I:%M %p")
        clock.config(text=time_now)
        weather_name.config(text="CURRENTLY")

        # Requesting for the weather with its api
        api = (
            "http://api.openweathermap.org/data/2.5/weather?q="
            + city
            + "&APPID=6a2cba9d48489b43b505644202086821"
        )
        data = requests.get(api).json()
        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        temp = int(data["main"]["temp"] - 273.15)
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["main"]["temp"]

        t.config(text=(temp, "ºC"))
        c.config(text=condition)
        w.config(text=wind)
        p.config(text=pressure)
        h.config(text=humidity)
        d.config(text=description)
    except:
        messagebox.showerror("Location Error!", "cannot find location\n check spelling")


# search icon
search_icon = PhotoImage(file="search_icon.png")
search_icon_image = Button(
    image=search_icon, background="#404040", width=0, cursor="hand2", command=getWeather
)
search_icon_image.place(x=310, y=30)

# app icon
# root.iconbitmap("weather icon.png")
app_icon = PhotoImage(file="weather icon.png")
root.iconphoto(False, app_icon)


# Logo in app, will be changed to a gif later in the upcoming versions
logo = PhotoImage(file="logo.png")
logo_image = Label(image=logo)
logo_image.place(x=150, y=100)

# Labellings
wd = Label(root, text="WIND", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white")
wd.place(x=80, y=380)

humid = Label(
    root, text="HUMIDITY", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white"
)
humid.place(x=180, y=380)

descript = Label(
    root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white"
)
descript.place(x=330, y=380)

press = Label(
    root, text="PRESSURE", font=("Helvetica", 15, "bold"), bg="#1ab5ef", fg="white"
)
press.place(x=520, y=380)

w = Label(text="...", font=("times new roman", 18, "bold"), bg="#1ab5ef")
w.place(x=75, y=410)

p = Label(text="...", font=("times new roman", 18, "bold"), bg="#1ab5ef")
p.place(x=530, y=410)

h = Label(text="...", font=("times new roman", 18, "bold"), bg="#1ab5ef")
h.place(x=200, y=410)

d = Label(text="...", font=("times new roman", 18, "bold"), bg="#1ab5ef")
d.place(x=330, y=410)

# Time
weather_name = Label(root, font=("Times New Roman", 20, "bold"))
weather_name.place(x=40, y=100)
clock = Label(root, font=("arial", 20, "bold"))
clock.place(x=50, y=140)

# Placing temperature and condition
t = Label(font=("Arial", 30, "bold"), fg="red")
t.place(x=500, y=100)

c = Label(font=("Arial", 28, "bold"))
c.place(x=500, y=150)

root.mainloop()

SystemExit
