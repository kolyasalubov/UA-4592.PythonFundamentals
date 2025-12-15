# HW 09 
# Task 3

import tkinter as tk
from tkinter import font
import threading
from OWM_file import get_weather_info

HEIGHT = 350
WIDTH = 550

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
                   bg="gray", fg="black", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

# ---
def format_weather_text(place: str, data: dict) -> str:
    return (
        f"Location: {place}\n"
        f"Status: {data.get('status')}\n"
        f"Temperature: {data.get('temp')} °C  (min: {data.get('temp_min')} °C, max: {data.get('temp_max')} °C)\n"
        f"Humidity: {data.get('humidity')} %\n"
        f"Wind: {data.get('wind_speed')} m/s, deg: {data.get('wind_deg')}\n"
        f"Clouds: {data.get('clouds')} %\n"
        f"Rain: {data.get('rain') if data.get('rain') else 'No data'}"
    )

# worker thread: calls API and updates label via label.after to run on main thread
def worker(place: str):
    result = get_weather_info(place)
    if result.get("ok"):
        text = format_weather_text(place, result["data"])
    else:
        text = f"Error fetching data for '{place}'.\nCheck city name or connection.\n\nDetails: {result.get('error')}"
    # update label in the main thread
    label.after(0, lambda: label.config(text=text))

# callback for button press: validates input and starts a background thread
def get_weather_command():
    place = entry_field.get().strip()
    if not place:
        messagebox.showinfo("Info", "Please enter a city (e.g. 'Chernivtsi,UA', 'London,GB').")
        return
    label.config(text="Loading...")
    t = threading.Thread(target=worker, args=(place,), daemon=True)
    t.start()

# connect button to command
button.config(command=get_weather_command)
# ---


root.mainloop()
