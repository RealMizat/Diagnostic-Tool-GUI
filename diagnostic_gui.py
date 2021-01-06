import os
from tkinter import *


def call_diag():
    os.system("dxdiag.exe")

root = Tk()

button = Button(root, text="PC Specs", command = call_diag)

button.grid(row = 2, column = 1)
root.geometry("300x175")
root.mainloop()
    

