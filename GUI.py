from tkinter import *
from tkinter.font import *
from PIL import ImageTk,Image ;




main_window = Tk()
bt_image=ImageTk.PhotoImage(Image.open("./search.png"))
main_window.iconbitmap("./RA.gif")
# set Title for main window.
main_window.title("Products & Systems Assurance ")
# change the icon of the window.
# main_window.iconphoto("E:\\Photos\\test.ico");
# font for GUI elements
font = Font(family="Calibri", size=12)
# create a label
label = Label(main_window, text="User National ID :", font=font)
# arrange the elements in grid.
label.grid(row=0, column=0)
# change the color of the label.
label.config(fg="#FF00FF")
# change the font
user_Nation_id_box = Entry( fg="#0000FF",
                           width=14,borderwidth=5)
user_Nation_id_box.insert(0,"Enter your national ID")
user_Nation_id_box.grid(row=0, column=1)
label.config()
#lablel frame
our_label=LabelFrame(text="User Information")
our_label.grid(row=2,column=0)
sys_name=StringVar()
sys_name.set("IM")
button_forth=Button(our_label,text="Group")
button_forth.grid(row=0,column=0)
am_radio_button=Radiobutton(our_label,variable=sys_name,value="AM",text="AM")
am_radio_button.grid(row=1,column=0);
im_radio_button=Radiobutton(our_label,variable=sys_name,value="IM",text="IM")
im_radio_button.grid(row=1,column=1);
om_radio_button=Radiobutton(our_label,variable=sys_name,value="OM",text="OM")
om_radio_button.grid(row=1,column=2);
def my_click():
    print(user_Nation_id_box.get())
# Button
search_Button = Button(text="Search ", padx=10, command=my_click, fg="#FF0000",
                       bg="#FFFFFF",image=bt_image)
search_Button.grid(row=0, column=2)
#main_window.iconbitmap('./risk.ico')
main_window.mainloop()
