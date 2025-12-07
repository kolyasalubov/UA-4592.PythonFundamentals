# You need combine two programs OWM.py and Tk_OWM.py
# into one working program.

import tkinter as tk
from OWM import get_weather
from tkinter import font

HEIGHT = 350
WIDTH = 450


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

city_var = tk.StringVar()
result = tk.StringVar()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, textvariable = city_var, font=('Arial', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Arial', 8), 
                   command=lambda: result.set(get_weather(city_var.get())))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, textvariable=result, font=('Arial', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()