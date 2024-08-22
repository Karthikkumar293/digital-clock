import tkinter as tk
from time import strftime

root = tk.Tk() 
root.title("KARTHIK DIGITAL CLOCK")

def time():
    string = strftime ('%H:%M:%S %p \n %m/%d/%Y ')
    label.config(text=string)
    label.after(1000,time)

label =tk.Label(root,font=('calibri' ,50,'bold'),background = 'red',  foreground ='black')
label.pack(anchor ='center')

time()

root.mainloop()




