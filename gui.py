import sys
import os
import tkinter as tk
from tkinter import ttk
import sv_ttk
import patient.gui_functions as gf
from tkinter import messagebox
print(sys.version)

def validate_login(window, user, password):
    user = user.get()
    passwd = password.get()
    result = gf.validate_login(user,passwd)
    if result[0] == 1:
        mainWindow.destroy()
        gf.logged_in()
    else:
        messagebox.showerror(title='Error', message="You entered wrong credentials.")
        #rejected.pack()



auth = 0
priviledge = 0

#main login screen

mainWindow = tk.Tk()
welcome_text = ttk.Label(mainWindow, text="Hospital DBMS", font='12px')
welcome_text.pack(padx=50, pady=35)
loginLabel1 = ttk.Label(mainWindow, text="Login using your credentials.")
loginLabel1.pack(padx=25, pady=25)

username = ttk.Entry(mainWindow)
username.pack(padx=25, pady=3)

passwrd = ttk.Entry(mainWindow, show="*")
passwrd.pack(padx=25, pady=3)

submit = ttk.Button(mainWindow, text="Login", command=lambda : validate_login(mainWindow, username, passwrd))
submit.pack(padx=25, pady=20)

sv_ttk.set_theme("light")

mainWindow.mainloop()



