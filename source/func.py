import tkinter as tk
from tkinter import BOTH, END, LEFT, RIGHT, Y, ttk
import hashlib
from components import *
from db import *

def check_create_new_user(parent, username,password, password_repeat):
    user_exists = False
    if(len(username) > 0):
        data = get_data()
        for i in data:
            if(i[0] == username):
                user_exists = True
        if user_exists:
            rel_label(parent,relheight=0.07, relwidth=1, relx=0.5, rely=0.79,text="User Exists!", bg="#e74c3c")
            return False
        else:
            if(len(password) > 0):
                if(password == password_repeat):
                    password = hashlib.sha256(password.encode('ascii')).hexdigest()
                    create_user(username, password)
                    rel_label(parent,relheight=0.07, relwidth=1, relx=0.5, rely=0.79,text="User Created Succesfully!", bg="#2ecc71")
                    rel_btn(parent,command= parent.destroy,relwidth=0.3,relheight=0.1,relx=0.5,rely=0.9,text="Done")
                    return True
                else:
                    rel_label(parent,relheight=0.07, relwidth=1, relx=0.5, rely=0.79,text="Please Check Your Password!", bg="#e74c3c")
                    return False
            else:
                rel_label(parent,relheight=0.07, relwidth=1, relx=0.5, rely=0.79,text="Please Enter Password!", bg="#e74c3c")
                return False
    else:
            rel_label(parent,relheight=0.07, relwidth=1, relx=0.5, rely=0.79,text="Please Enter Username!", bg="#e74c3c")
            return False

def new_user():
    win = tk.Toplevel()
    win.wm_title("New User")
    win.maxsize(300,300)
    win.minsize(300,300)
    icon = tk.PhotoImage("assets//icon_transparent.ico")
    win.iconbitmap(icon)

    u_name = None
    p_word = None
    p_repeat = None

    rel_label(win,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text="Enter User Credentials")

    rel_label(win,relheight=0.07, relwidth=0.5, relx=0.5, rely=0.2,text="Username")
    u_name = input_line(win,u_name,relx=0.5,rely=0.28,width=150,height=28)

    rel_label(win,relheight=0.07, relwidth=0.5, relx=0.5, rely=0.4,text="Password")
    p_word = input_line_secret(win,p_word,relx=0.5,rely=0.48,width=150,height=28)

    rel_label(win,relheight=0.07, relwidth=0.5, relx=0.5, rely=0.6,text="Password Repeat")
    p_repeat = input_line_secret(win,p_repeat,relx=0.5,rely=0.68,width=150,height=28)

    rel_btn(win,command= lambda : check_create_new_user(win,u_name.get(),p_word.get(),p_repeat.get()),relwidth=0.3,relheight=0.1,relx=0.5,rely=0.9,text="Create")

def check_cred(root,u_name,p_word):
    data = get_data()
    user_found = False
    for i in data:
        if(u_name == i[0] and hashlib.sha256(p_word.encode('ascii')).hexdigest() == i[1]):
            user_found = True
    if user_found:
        #popUp("Login Succesful!")
        list_password(root,u_name)
    else:
        popUp("Invalid Credentials!")

def hello():
    popUp("Hello World!!!")

def about():
    info = "BPM is a password manager made by dekaottoman\nas an OSS (Open-Source Software) contribution\nand as an exercise for other python learners."
    popUp(info)

def password_check(self,username:str,new_pword:str,new_pword_repeat:str,old_password:str):
    if(new_pword == new_pword_repeat):
        if(old_password == get_password(username)):
            change_password(username,new_pword)
            canvas = tk.Canvas(self, bg="#f0f0f0")
            canvas.place(relheight=1,relwidth=1)
            rel_label(self,relheight=0.2, relwidth=1, relx=0.5, rely=0.4,text="Your Password Has\nBeen Successfully Changed!")
            rel_btn(self,command= self.destroy,relwidth=0.5,relheight=0.2,relx=0.5,rely=0.8,text="Done")
        else:
            rel_label(self,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text=("Invalid Password!"), bg="#e74c3c")
    else:
        rel_label(self,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text=("Please Check Your New Password!"), bg="#e74c3c")

def user_manage_password(self,username):
    self.minsize(300,300)
    self.maxsize(300,300)
    password = None
    new_pword = None
    new_pword_repeat = None
    canvas = tk.Canvas(self, bg="#f0f0f0")
    canvas.place(relheight=1,relwidth=1)
    rel_label(self,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text=("Logged in as : %s"%username))
    rel_label(self,relheight=0.1, relwidth=0.5, relx=0.5, rely=0.2,text=("Old Password"))
    password = input_line_secret(self,password,relx=0.5,rely=0.3,width=150,height=25)
    rel_label(self,relheight=0.1, relwidth=0.5, relx=0.5, rely=0.4,text=("New Password"))
    new_pword = input_line_secret(self,new_pword,relx=0.5,rely=0.5,width=150,height=25)
    rel_label(self,relheight=0.1, relwidth=0.5, relx=0.5, rely=0.6,text=("New Password Repeat"))
    new_pword_repeat = input_line_secret(self,new_pword_repeat,relx=0.5,rely=0.7,width=150,height=25)
    rel_btn(self,command=lambda:password_check(self,username,hashlib.sha256(new_pword.get().encode('ascii')).hexdigest(),hashlib.sha256(new_pword_repeat.get().encode('ascii')).hexdigest(),hashlib.sha256(password.get().encode('ascii')).hexdigest()),relwidth=0.5,relheight=0.1,relx=0.5,rely=0.9,text="Change Password")

def username_check(self,username:str,new_username:str,password:str):
    if(password == get_password(username)):
        change_username(username,new_username)
        canvas = tk.Canvas(self, bg="#f0f0f0")
        canvas.place(relheight=1,relwidth=1)
        rel_label(self,relheight=0.2, relwidth=1, relx=0.5, rely=0.4,text=("Username '%s' has been\n changed to '%s'."%(username,new_username)))
        rel_btn(self,command= self.destroy,relwidth=0.5,relheight=0.2,relx=0.5,rely=0.8,text="Done")
    else:
        rel_label(self,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text=("Invalid Password!"), bg="#e74c3c")

def user_manage_username(self,username:str):
    new_uname = None
    password = None
    canvas = tk.Canvas(self, bg="#f0f0f0")
    canvas.place(relheight=1,relwidth=1)
    rel_label(self,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text=("Logged in as : %s"%username))
    rel_label(self,relheight=0.15, relwidth=0.5, relx=0.5, rely=0.26,text=("New Username"))
    new_uname = input_line(self,new_uname,relx=0.5,rely=0.37,width=150,height=25)
    rel_label(self,relheight=0.15, relwidth=0.5, relx=0.5, rely=0.51,text=("Password"))
    password = input_line_secret(self,password,relx=0.5,rely=0.62,width=150,height=25)
    rel_btn(self,command=lambda: username_check(self,username,new_uname.get(),hashlib.sha256(password.get().encode('ascii')).hexdigest()),relwidth=0.5,relheight=0.2,relx=0.5,rely=0.85,text="Change Username")

def delete_check(self,username:str,password:str):
    if(password == get_password(username)):
        delete_user(username)
        canvas = tk.Canvas(self, bg="#f0f0f0")
        canvas.place(relheight=1,relwidth=1)
        rel_label(self,relheight=0.2, relwidth=0.5, relx=0.5, rely=0.4,text=("User : %s \n has been deleted."%username))
        rel_btn(self,command= self.destroy,relwidth=0.5,relheight=0.2,relx=0.5,rely=0.8,text="Done")
    else:
        rel_label(self,relheight=0.2, relwidth=0.5, relx=0.5, rely=0.27,text=("Invalid Password!"), bg="#e74c3c")

def user_manage_delete(self, username:str):
    password = None
    canvas = tk.Canvas(self, bg="#f0f0f0")
    canvas.place(relheight=1,relwidth=1)
    rel_label(self,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text=("Logged in as : %s"%username))
    rel_label(self,relheight=0.2, relwidth=0.5, relx=0.5, rely=0.27,text=("WARNING! THIS ACTION \nCANNOT BE TAKEN BACK!"),bg="#e74c3c")
    rel_label(self,relheight=0.15, relwidth=0.5, relx=0.5, rely=0.46,text=("Password"))
    password = input_line_secret(self,password,relx=0.5,rely=0.57,width=150,height=25)
    rel_btn(self,command= lambda: delete_check(self,username, hashlib.sha256(password.get().encode('ascii')).hexdigest()),relwidth=0.5,relheight=0.2,relx=0.5,rely=0.8,text="Delete User")

def user_manage_check(self, username:str, password:str):
    user_exists = False
    logged_in_as = None
    data = get_data()
    for i in data:
        if (i[0] == username and i[1] == password):
            user_exists = True

    if user_exists:
        canvas = tk.Canvas(self, bg="#f0f0f0")
        canvas.place(relheight=1,relwidth=1)
        logged_in_as = username
        rel_label(self,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text=("Logged in as : %s"%username))
        rel_btn(self,command=lambda: user_manage_username(self,username),relwidth=0.5,relheight=0.2,relx=0.5,rely=0.3,text="Change Username")
        rel_btn(self,command=lambda: user_manage_password(self,username),relwidth=0.5,relheight=0.2,relx=0.5,rely=0.55,text="Change Password")
        rel_btn(self,command=lambda: user_manage_delete(self,logged_in_as),relwidth=0.5,relheight=0.2,relx=0.5,rely=0.8,text="Delete User")
    else:
        popUp("Invalid Credentials!")

def user_manage():
    win = tk.Toplevel()
    win.wm_title("User Management")
    win.maxsize(300,200)
    win.minsize(300,200)
    icon = tk.PhotoImage("assets//icon_transparent.ico")
    win.iconbitmap(icon)

    u_name = None
    p_word = None

    rel_label(win,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text="Enter User Credentials")

    rel_label(win,relheight=0.14, relwidth=0.5, relx=0.5, rely=0.27,text="Username")
    u_name = input_line(win,u_name,relx=0.5,rely=0.41,width=150,height=28)

    rel_label(win,relheight=0.14, relwidth=0.5, relx=0.5, rely=0.55,text="Password")
    p_word = input_line_secret(win,p_word,relx=0.5,rely=0.69,width=150,height=28)

    rel_btn(win,command= lambda: user_manage_check(win,u_name.get(),hashlib.sha256(p_word.get().encode('ascii')).hexdigest()),relwidth=0.3,relheight=0.2,relx=0.5,rely=0.88,text="Log In")

def new_password_check(root,self,username:str,title:str,site_username:str, email:str,password:str):
    if(len(title)>0):
        if (len(password) > 0):
            create_password(username,title,site_username,email,password)
            canvas = tk.Canvas(self, bg="#f0f0f0")
            canvas.place(relheight=1,relwidth=1)
            rel_label(self,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text="Password Created", bg="#2ecc71")
            rel_btn(self,command= self.destroy,relwidth=0.5,relheight=0.075,relx=0.5,rely=0.93,text="Done")
            list_password(root, username)
        else:
            rel_label(self,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text="Please Enter Password!", bg="#e74c3c")
    else:
        rel_label(self,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text="Please Enter a Title!", bg="#e74c3c")

def new_password(root,username):
    win = tk.Toplevel()
    win.wm_title("New User")
    win.maxsize(250,400)
    win.minsize(250,400)
    icon = tk.PhotoImage("assets//icon_transparent.ico")
    win.iconbitmap(icon)

    title = None
    email = None
    site_username = None
    p_word = None

    rel_label(win,relheight=0.1, relwidth=1, relx=0.5, rely=0.05,text="Logged in as : %s"%username)

    rel_label(win,relheight=0.07, relwidth=0.6, relx=0.5, rely=0.17,text="Title for Password")
    title = input_line(win,title,relx=0.5,rely=0.23,width=150,height=28)

    rel_label(win,relheight=0.07, relwidth=0.6, relx=0.5, rely=0.37,text="Email")
    email = input_line(win,email,relx=0.5,rely=0.43,width=150,height=28)

    rel_label(win,relheight=0.07, relwidth=0.6, relx=0.5, rely=0.57,text="Username")
    site_username = input_line(win,site_username,relx=0.5,rely=0.63,width=150,height=28)

    rel_label(win,relheight=0.07, relwidth=0.6, relx=0.5, rely=0.77,text="Password")
    p_word = input_line_secret(win,p_word,relx=0.5,rely=0.83,width=150,height=28)

    rel_btn(win,command=lambda:new_password_check(root,win,username,title.get(),site_username.get(),email.get(),p_word.get()),relwidth=0.5,relheight=0.075,relx=0.5,rely=0.93,text="Create")

def list_password(root, username):
    root.minsize(300,600)
    root.maxsize(300,600)
    canvas = tk.Canvas(root, bg="#f0f0f0")
    canvas.place(relheight=1,relwidth=1)
    rel_label(root,relheight=0.075, relwidth=1, relx=0.5, rely=0.0375,text=("Logged in as : %s"%username))
    rel_btn(root,command=lambda: new_password(root,username),relwidth=0.5,relheight=0.05,relx=0.25,rely=0.9,text="Create New Password")
    rel_btn(root,command=lambda:delete_password(root,username),relwidth=0.5,relheight=0.05,relx=0.75,rely=0.9,text="Delete a Password")
    rel_label(root,relheight=0.075, relwidth=1, relx=0.5, rely=0.9625,text=("By dekaottoman"))

    data = get_password_list(username)

    list_canvas = tk.Canvas(root,bg="#f0f0f0")
    list_canvas.place(relheight=0.8,relwidth=1,relx=0.5,rely=0.475,anchor=CENTER)

    scrollbar = ttk.Scrollbar(list_canvas)
    scrollbar.place(relheight=1,relwidth=0.5,rely=0.5,relx=0.975,anchor=CENTER)
    mylist = tk.Listbox(list_canvas, yscrollcommand = scrollbar.set ,bg="#f0f0f0")
    for i in data:
        mylist.insert(END, "Password Title : %s"%i[1])
        mylist.insert(END, "Username :%s"%i[2])
        mylist.insert(END, "Email : %s"%i[3])
        mylist.insert(END, "Password : %s"%i[4])
        mylist.insert(END, "")

    mylist.place(relwidth=0.95,relheight=1,relx=0.475,rely=0.5, anchor=CENTER)
    scrollbar.config( command = mylist.yview )

def delete_password_check(root,self,username:str,title:str,password:str):
    if(get_password(username) == password):
        delete_password_from_list(username,title)
        rel_label(self,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text="Password Deleted!", bg="#2ecc71")
        rel_btn(self,command= self.destroy,relwidth=0.3,relheight=0.2,relx=0.5,rely=0.88,text="Done")
        list_password(root, username)
    else:
        rel_label(self,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text="Please check your password!", bg="#e74c3c")

def delete_password(root,username:str):
    win = tk.Toplevel()
    win.wm_title("Password Deletion")
    win.maxsize(300,200)
    win.minsize(300,200)
    icon = tk.PhotoImage("assets//icon_transparent.ico")
    win.iconbitmap(icon)

    p_title = None
    p_word = None

    rel_label(win,relheight=0.15, relwidth=1, relx=0.5, rely=0.075,text="Enter Details")

    rel_label(win,relheight=0.14, relwidth=0.5, relx=0.5, rely=0.27,text="Password Title")
    p_title = input_line(win,p_title,relx=0.5,rely=0.41,width=150,height=28)

    rel_label(win,relheight=0.14, relwidth=0.5, relx=0.5, rely=0.55,text="User Password")
    p_word = input_line_secret(win,p_word,relx=0.5,rely=0.69,width=150,height=28)

    rel_btn(win,command= lambda: delete_password_check(root,win,username,p_title.get(),hashlib.sha256(p_word.get().encode('ascii')).hexdigest()),relwidth=0.3,relheight=0.2,relx=0.5,rely=0.88,text="Delete")