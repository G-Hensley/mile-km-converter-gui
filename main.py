from tkinter import *
FONT = ("Arial", 14)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)
window.config(padx=15, pady=15)


def convert_miles():
    miles = float(mile_input.get())
    km = str(round(miles * 1.609344, 2))
    km_num.config(text=km)


mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=3, row=1)
mile_label.config(pady=5, padx=5)

mile_input = Entry()
mile_input.config(width=15)
mile_input.grid(column=2, row=1)

is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=1, row=2)
is_equal_label.config(padx=5, pady=5)

km_num = Label(text="0", font=FONT)
km_num.grid(column=2, row=2)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=3, row=2)

calc_button = Button(text="Calculate", font=FONT, command=convert_miles)
calc_button.grid(column=2, row=3)

window.mainloop()