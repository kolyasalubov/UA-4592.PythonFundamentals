import tkinter as tk
from tkinter import font
from pyowm.owm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(location): 
    observation = mgr.weather_at_place(location)
    w = observation.weather

    weather_info = f"Location: {location}\n" 
    weather_info += f"Status: {w.detailed_status}\n"
    weather_info += f"Wind: {w.wind()}\n" 
    weather_info += f"Humidity: {w.humidity}\n"
    weather_info += f"Temperature: {w.temperature('celsius')['temp']} C\n" 
    weather_info += f"Rain: {w.rain}\n"
    weather_info += f"Heat index: {w.heat_index}\n"
    weather_info += f"Clouds: {w.clouds}"
    
    label.config(text=weather_info)


HEIGHT = 550
WIDTH = 750


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()