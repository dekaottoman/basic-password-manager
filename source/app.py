import tkinter as tk
from tkinter import ttk
from components import *
from db import *
from func import *

root = tk.Tk()
root.minsize(300,600)
root.maxsize(300,600)
root.title("BPM")
icon = tk.PhotoImage("assets//icon_transparent.ico")
root.iconbitmap(icon)

username = None
password = None

rel_label(root,relheight=0.075, relwidth=1, relx=0.5, rely=0.0375,text="BPM - Basic Password Manager")

img = tk.PhotoImage(file="assets//logo_transparent_200x200.png")
logo = tk.Label(root, image=img)
logo.place(width=200, height=200 , rely=0.25, relx=0.5, anchor=CENTER)

rel_label(root,relheight=0.05, relwidth=0.5, relx=0.5, rely=0.45,text="Username")
username = input_line(root,username,relx=0.5,rely=0.49,width=150,height=25)
rel_label(root,relheight=0.05, relwidth=0.5, relx=0.5, rely=0.54,text="Password")
password = input_line_secret(root,password,relx=0.5,rely=0.58,width=150,height=25)
rel_btn(root,command = lambda: check_cred(root,username.get(), password.get()),relwidth=0.5,relheight=0.05,relx=0.5,rely=0.635,text="Log In")
rel_btn(root,new_user,relwidth=0.5,relheight=0.05,relx=0.5,rely=0.69,text="Create New Local User")


rel_btn(root,user_manage,relwidth=0.5,relheight=0.05,relx=0.5,rely=0.83,text="Manage User")
rel_btn(root,about,relwidth=0.5,relheight=0.05,relx=0.5,rely=0.88,text="About")

rel_label(root,relheight=0.075, relwidth=1, relx=0.5, rely=0.9625,text="By dekaottoman")

if __name__ == "__main__":
    create_db()
    
    root.mainloop()