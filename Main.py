
from time import localtime
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import  TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

win=Tk()
win.title("mero weather app")
win.geometry("900x500")
win.resizable(False,False)
# win.configure(bg="Light blue")

def weather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent='geoapiExcercises')
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        home = pytz.timezone(result)
        localtime = datetime.now(home)
        current_time = localtime.strftime("%I:%M:%S %p")
        clock.config(text=current_time)
        name.config(text='CURRENT WEATHER')

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=34cb20a1853f9a6c4cb5f1dafb8b67ef"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Assuming 't', 'c', 'w', 'p' are defined as Label widgets
        t.config(text=f"{temp}°")  # Set temperature with degree symbol
        c.config(text=f"{condition} | Feels Like {temp}°")  # Set weather condition and feels like temperature
        w.config(text=f'{wind}')  # Set weather description
        p.config(text=pressure)  # Set pressure
        h.config(text=f"Humidity: {humidity}%")  # Assuming humidity is in percentage
        d.config(text=f"Description: {description}")  # Set the description
    except Exception as e:
        messagebox.showerror('error occured',e)

#Images
search_box=PhotoImage(file='Copy of search.png')
search_icon=PhotoImage(file='Copy of search_icon.png')
Logo = Image.open("Logo.png")
box=PhotoImage(file='Copy of box.png')

#Search box
myimage = Label(win, image=search_box)
myimage.place(x=20, y=20)  # Use place to position the label

textfield=tk.Entry(win,justify='center',width=17,font=('poppins',25,"bold"),fg='light blue',bg='#404040',border=0)
textfield.place(x=95,y=40)
textfield.focus()

myimage_icon=Button(image=search_icon,borderwidth=0,cursor='cross',bg='#404040',command=weather)
myimage_icon.place(x=400,y=34)

#Logo
photo= ImageTk.PhotoImage(Logo)
label = Label(win, image=photo)
label.place(x=90,y=100)

#Description box
Mybox=Label(image=box).pack(padx=5,pady=5,side='bottom')

name=Label(win,font=('arial',15,'bold'))
name.place(x=30,y=100)
clock=Label(win,font=('arial',20))
clock.place(x=30,y=130)


#Labels
# label1=label(win,text='Wind',font=("Helvetica",20,"bold"),fg='white')
label1 = tk.Label(win, text='Wind', font=("Helvetica", 20, "bold"), fg='Black',bg='#eee4b1')
label1.place(x=120,y=400)

label2 = tk.Label(win, text='Humidity', font=("Helvetica", 20, "bold"), fg='Black',bg='#eee4b1')
label2.place(x=225,y=400)

label3 = tk.Label(win, text='Description', font=("Helvetica", 20, "bold"), fg='Black',bg='#eee4b1')
label3.place(x=430,y=400)

label4 = tk.Label(win, text='Pressure', font=("Helvetica", 20, "bold"), fg='Black',bg='#eee4b1')
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg='#ee666d')
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text='....',font=('arial',14,'bold'),bg='#eee4b1', fg='Black')
w.place(x=120,y=430)
h=Label(text='....',font=('arial',14,'bold'),bg='#eee4b1', fg='Black')
h.place(x=225,y=430)
d=Label(text='....',font=('arial',14,'bold'),bg='#eee4b1', fg='Black')
d.place(x=430,y=430)
p=Label(text='....',font=('arial',14,'bold'),bg='#eee4b1', fg='Black')
p.place(x=650,y=430)





win.mainloop()
