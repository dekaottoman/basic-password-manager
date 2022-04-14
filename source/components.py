import tkinter as tk
from tkinter import CENTER, ttk

def popUp(msg:str, title:str = "For you!", height:int = 150, width:int = 300):
    win = tk.Toplevel()
    win.wm_title(title)
    win.maxsize(width,height)
    win.minsize(width,height)
    icon = tk.PhotoImage("assets//icon_transparent.ico")
    win.iconbitmap(icon)

    l = tk.Label(win, text=msg)
    l.place(relwidth=1, relheight=0.3, rely=0.15, relx=0)

    b = ttk.Button(win, text="OK", command=win.destroy)
    b.place(relwidth=0.3, relheight=0.2, rely=0.6, relx=0.35)

def rel_btn(master,command,relwidth:float,relheight:float,relx:float,rely:float,text:str):
    button = ttk.Button(master, text=text,command=command)
    button.place(relwidth=relwidth, relheight=relheight, rely=rely, relx=relx, anchor=CENTER)

def input_line(master,input_id,relx:float,rely:float,width:int = 150,height:int = 20):
    input_id = ttk.Entry(master,justify='center')
    input_id.place(relx=relx,rely=rely,anchor=CENTER, width=width,height=height)
    return input_id

def input_line_secret(master,input_id,relx:float,rely:float,width:int = 150,height:int = 20):
    input_id = ttk.Entry(master, show="*",justify='center')
    input_id.place(relx=relx,rely=rely,anchor=CENTER, width=width,height=height)
    return input_id

def rel_label(master, relwidth:int ,relheight:int, relx:int ,rely:int,text:str = "Some Text",bg:str = "#252a35", fg:str = "#f0f0f0"):
    label = tk.Label(master, text=text, bg=bg, fg=fg)
    label.place(relheight=relheight, relwidth=relwidth, relx=relx, rely=rely, anchor=CENTER)