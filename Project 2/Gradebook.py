from tkinter import *
#import tkinter as tk
from tkinter import ttk
#Gradebook: Store, modify, and calculate student grades.
# calc GPA
# calc Grade in class
root = Tk()
root.title("Gradebook")


mainframe = ttk.Frame(root, padding="7 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



root.mainloop()