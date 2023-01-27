# Importing Tkinter library
# in the environment
from tkinter import *

# Creating a window
window = Tk()
window.title("Theme Changer")
window.geometry("720x480+300+200")
window.config(bg="white")


# Adding light and dark mode images
light = PhotoImage(file="light.png")
dark = PhotoImage(file="dark.png")

switch_value = True

# Defining a function to toggle
# between light and dark theme
def toggle():

	global switch_value
	if switch_value == True:
		switch.config(image=dark, bg="#26242f",
					activebackground="#26242f")
		
		# Changes the window to dark theme
		window.config(bg="#26242f")
		switch_value = False

	else:
		switch.config(image=light, bg="white",
					activebackground="white")
		
		# Changes the window to light theme
		window.config(bg="white")
		switch_value = True


# Creating a button to toggle
# between light and dark themes
switch = Button(window, image=light,
				bd=0, bg="white",
				activebackground="white",
				command=toggle)
switch.place(x=430, y=20)

window.mainloop()
