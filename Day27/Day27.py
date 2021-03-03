from tkinter import *

def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    label2.config(text="{:.2f}".format(km))

window = Tk()
window.minsize(width=200,height=100)
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)

entry = Entry(width=1)
entry.insert(END,"0")
entry.grid(column=1, row=0)
entry.config(width=5)
entry.focus()

label2 = Label(text="0.00")
label2.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

label3 = Label(text="Miles")
label3.grid(column=2, row=0)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

window.mainloop()