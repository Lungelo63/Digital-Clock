from tkinter import Tk
from tkinter import LabelFrame
import time
import sys

master = Tk()
master.title("DigitalClock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text = timeVar)
    clock.after(200,get_time)

LabelFrame(master,font = ("Arial",30), text = "Digital Clock",fg = "white", bg = "black").pack()
clock = LabelFrame(master, font = ("Arial", 90), bg = "grey", fg = "white")
clock.pack()

get_time( )

master.mainloop()
