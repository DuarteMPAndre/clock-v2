from tkinter import *
from tkinter.ttk import *

from time import strftime
import time

root = Tk()
root.title("Clock")
root.iconbitmap(r'C:\Users\Utilizador\Downloads\clock_icon.ico')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background= "black", foreground="blue")
label.pack(anchor='center', expand= TRUE, fill = BOTH)
time()

mainloop()