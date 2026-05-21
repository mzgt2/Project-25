from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

def calculate():
    user_input = float(entry.get())
    km = round(float(user_input * 1.609344), 2)
    label_4.config(text=f"{km}")



label_1 = Label(text="Miles")
label_1.grid(column=4, row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)
#
label_3 = Label(text="Km")
label_3.grid(column=4, row=2)
#
label_4 = Label(text="0")
label_4.grid(column=3, row=2)
#
button = Button(text="Calculate", command=calculate)
button.grid(column=3, row=3)
#
entry = Entry(width=10)
entry.grid(column=3, row=1)

spacer_1 = Label(text=" ")
spacer_1.grid(column=0, row=0)

spacer_2 = Label(text=" ")
spacer_2.grid(column=0, row=2)

window.mainloop()
