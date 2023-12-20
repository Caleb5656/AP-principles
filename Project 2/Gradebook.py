
import tkinter as tk
import tkinter.messagebox
from tkinter import END, ttk
#Gradebook: Store, modify, and calculate student grades.
# calc GPA
# calc Grade in class
def get_name():
    stu_name = stu_add_txt.get()
    if stu_name == "":
        msg="Enter a students name first!"
        tkinter.messagebox.showinfo("Error", msg)
    else:
        global sched_tab
        sched_tab = ttk.Frame(tab_control)
        tab_control.add(sched_tab, text=stu_name)
        tab_control.pack(expand=1, fill="both")
        stu_add_txt.delete(0, END)

root = tk.Tk()
root.geometry("300x300")
root.title("Gradebook")
root.configure(bg="red")
tab_control = ttk.Notebook(root)

reg_tab = ttk.Frame(tab_control)
tab_control.add(reg_tab, text='Register')

tab_control.pack(expand=1, fill="both")
# mainframe = ttk.Frame(root, padding="3 3 12 12")
# mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

stu_add_lbl = tk.Label(reg_tab,text="Enter the students name into the box", bg='blue')
stu_add_lbl.pack()
stu_add_txt = tk.Entry(reg_tab,borderwidth=5)
stu_add_txt.pack()

stu_add_btn = tk.Button(reg_tab, text="Add Student", command=get_name, bg='grey', width=10, height=4)
stu_add_btn.place(x=150,y=-32)
stu_add_btn.pack()




sched = []
# while len(sched) < 8:

root.mainloop()