from tkinter import Entry

def ReadInfo(User:Entry,Password:Entry):
    global username,password
    username = User.get()
    password = Password.get()