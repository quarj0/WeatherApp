import requests
from tkinter import *
from tkinter import messagebox

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500")
        self.root.title("Weather App")
        self.root.iconbitmap("weather icon.png")
        self.root.resizable(False, False)
        self.root.config(bg="#FFFFFF")

        # Background Image
        self.bg = PhotoImage(file="logo.png")
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # City Label
        self.city_label = Label(
            self.root,
            text="Enter city name:",
            font=("Helvetica", 16),
            bg="#FFFFFF",
            fg="#555555",
        )
        self.city_label.pack(pady=20)

        # City Menu
        self.city_var = StringVar()
        self.city_menu = Entry(
            self.root,
            textvariable=self.city_var,
            font=("Helvetica", 16),
            bg="#FFFFFF",
            fg="#555555",
            relief="solid",
            bd=0,
            highlightthickness=1,
            highlightcolor="#555555",
            highlightbackground="#555555",
        )
        self.city_menu.pack()

        # Submit Button
        self.submit_button = Button(
            self.root,
            text="Submit",
            font=("Helvetica", 16),
            bg="#555555",
            fg="#FFFFFF",
            activebackground="#FFFFFF",
            activeforeground="#555555",
            relief="solid",
            bd=0,
            command=self.get_weather_update,
        )
        self.submit_button.pack(pady=20)

        # Weather Label
        self.weather_label = Label(
            self.root,
            text="",
            font=("Helvetica", 16),
            bg="#FFFFFF",
            fg="#555555",
        )
        self.weather_label.pack(pady=20)

    def get_weather_update(self):
        city = self.city_var.get()
        if city == "":
            messagebox.showerror("Error", "Please enter a city name.")
            return

        # API call
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=6a2cba9d48489b43b505644202086821"
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Error", "Could not fetch weather data. Please try again later.")
            return

        weather_data = response.json()
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].title()

        self.weather_label.config(text=f"{city}: {temp}°C, {description}")

root = Tk()
weather_app = WeatherApp(root)
root.mainloop()
