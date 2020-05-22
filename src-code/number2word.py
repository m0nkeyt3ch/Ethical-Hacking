import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
import inflect

win = tk.Tk()


def convert():
    number = entry.get()
    i = inflect.engine()
    word = i.number_to_words(number)
    showinfo("Word", f"{number} = {word.title()}")


label = tk.Label(win, text="Enter number here: ")
label.grid(row=0, column=0)

entry = tk.Entry(win, bg="#1DFD9B")
entry.grid(row=0, column=1, padx=10, pady=5)

button = ttk.Button(win, text="Go", command=convert)
button.grid(row=1, column=0, columnspan=2)

win.mainloop()
