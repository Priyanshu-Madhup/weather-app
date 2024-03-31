#MODULES BEING IMPORTED
from datetime import timezone
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import *
import requests
import pytz
from PIL import Image, ImageTk
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

#CREATING MAIN FRAME NAMED ROOT
root = Tk()
root.title("Weather Forecast")
root.geometry("890x470")
root.configure(bg="#57adff")
root.resizable(False, False)

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="weatherforecast")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.configure(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")
    
#background_image = PhotoImage(file="Images/background_image (1).png")

# Create a label with the image
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

#CREATING THE TOP WEATHER FORECAST LOGO
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

#ROUND RECTANGLE TO DISPLAY INFORMATION
Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)

#LABEL1 
label1 = Label(root, text="Temperature", font=('Helvitica 93', 11), fg="white", bg="#203243")
label1.place(x=50, y=120)

#LABEL2
label2 = Label(root, text="Humidity", font=('Helvitica 93', 11), fg="white", bg="#203243")
label2.place(x=50, y=140)

#LABEL3
label3 = Label(root, text="Pressure", font=('Helvitica 93', 11), fg="white", bg="#203243")
label3.place(x=50, y=160)

#LABEL3
label3 = Label(root, text="Wind Speed", font=('Helvitica 93', 11), fg="white", bg="#203243")
label3.place(x=50, y=180)

#LABEL4
label4 = Label(root, text="Description", font=('Helvitica', 11), fg="white", bg="#203243")
label4.place(x=50, y=200)

#SEARCH OPTION
Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="Images/Layer 7.png")
weatherimage = Label(root, image=weat_image, bg="#203243")
weatherimage.place(x=290, y=127)

#ENTRY BOX
textfield = tk.Entry(root, justify='center', width=13, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=360, y=130)
textfield.focus()

#SEARCH ICON WITH BUTTON
Search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=125)

#BOTTOM BOX
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

#
firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

clock = Label(root, font=("Helvitica", 20), fg="white", bg="#57adff")
clock.place(x=30, y=20)
timezone = Label(root, font=("Helvitica", 20), fg="black", bg="#57adff")
timezone.place(x=650, y=20)
long_lat = Label(root, font=("Helvitica", 10), fg="white", bg="#57adff")
long_lat.place(x=650, y=60)

root.mainloop()