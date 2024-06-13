from tkinter import Entry
from core import Mangement

def ReadInfo(User:Entry,Password:Entry):
    global username,password
    username = User.get()
    password = Password.get()

def New(username:str,height:float):
    Mangement(username).new([height]) if username != "" else None