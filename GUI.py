import threadsafe_tkinter as tk
import tkinter as tkm
from tkinter.font import *;
main_window=tkm.Tk()
#set Title for main window.
main_window.title("Application Development ")
#change the icon of the window.
#main_window.iconphoto("E:\\Photos\\test.ico");
#font for GUI elements
font=Font(family="Calibri",size=12);
#create a label
label=tk.Label(main_window,text="User National ID :",font=font)
#arrange the elements in grid.
label.grid(row=0,column=0)
#change the color of the label.
label.config(fg="#FF00FF");
#change the font

label.config()
main_window.mainloop()
