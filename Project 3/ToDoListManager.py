import tkinter as tk
import tkinter.messagebox
from tkinter import END, ttk

def add():
  with open("toDoList", "w") as f:
    f.write(input())


root = tk.Tk()
root.geometry("300x300")
root.title("To Do List")
tab_control = ttk.Notebook(root)

add_tab = ttk.Frame(tab_control)
tab_control.add(add_tab, text='Add')
tab_control.pack(expand=1, fill="both")

rem_tab = ttk.Frame(tab_control)
tab_control.add(rem_tab, text='Remove')
tab_control.pack(expand=1, fill="both")

view_tab = ttk.Frame(tab_control)
tab_control.add(view_tab, text='View List')
tab_control.pack(expand=1, fill="both")
root.mainloop()
# with open("toDoList", "w") as f:
#   f.write(input())