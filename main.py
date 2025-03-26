"""
Mile to Kilometer Converter
A simple GUI application that converts between miles and kilometers.
The program provides a user interface with input field and allows
switching between conversion directions.
"""

from tkinter import *
import tkinter as tk
FONT = ("Arial", 14)

# Initialize the main window and set its properties
window = Tk()
window.title("Mile/Km Converter")
window.minsize(width=300, height=150)
window.config(padx=15, pady=15)

# Global variables for conversion direction
converting_to_km = True

"""
Conversion Functions
These functions handle the conversion logic and user input processing
"""
def convert():
    try:
        if converting_to_km:
            miles = float(mile_input.get())
            km = str(round(miles * 1.609344, 2))
            km_num.config(text=km)
        else:
            km = float(km_input.get())
            miles = str(round(km / 1.609344, 2))
            miles_num.config(text=miles)
    except ValueError:
        result_label.config(text="Please enter a valid number")

def switch_conversion():
    global converting_to_km
    converting_to_km = not converting_to_km
    
    if converting_to_km:
        mile_input.grid()
        mile_label.grid()
        km_input.grid_remove()
        km_label.grid()
        miles_num.grid_remove()
        km_num.grid()
        result_label.config(text="Miles to Kilometers")
    else:
        mile_input.grid_remove()
        mile_label.grid_remove()
        km_input.grid()
        km_label.grid()
        km_num.grid_remove()
        miles_num.grid()
        result_label.config(text="Kilometers to Miles")

def on_enter(event):
    convert()

"""
GUI Elements
Creating and configuring all the visual elements of the application
"""
# Title and direction label
result_label = Label(text="Miles to Kilometers", font=FONT)
result_label.grid(column=0, row=0, columnspan=4, pady=10)

# Input section
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=3, row=1)
mile_label.config(pady=5, padx=5)

mile_input = Entry()
mile_input.config(width=15)
mile_input.grid(column=2, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=3, row=1)
km_label.config(pady=5, padx=5)
km_label.grid_remove()  # Initially hidden

km_input = Entry()
km_input.config(width=15)
km_input.grid(column=2, row=1)
km_input.grid_remove()  # Initially hidden

# Output section
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=1, row=2)
is_equal_label.config(padx=5, pady=5)

km_num = Label(text="0", font=FONT)
km_num.grid(column=2, row=2)

miles_num = Label(text="0", font=FONT)
miles_num.grid(column=2, row=2)
miles_num.grid_remove()  # Initially hidden

# Control section
calc_button = Button(text="Calculate", font=FONT, command=convert)
calc_button.grid(column=2, row=3)

switch_button = Button(text="Change Unit", font=FONT, command=switch_conversion)
switch_button.grid(column=2, row=4, pady=10)

# Bind Enter key to trigger conversion
window.bind_all("<Return>", on_enter)

# Start the application
window.mainloop()