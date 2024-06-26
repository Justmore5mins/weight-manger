from tkinter import Entry
from core import Mangement

def ReadInfo(User:Entry,Password:Entry):
    global username,password
    username = User.get()
    password = Password.get()

def New(username:str,height:float):
    Mangement(username).new([height]) if username != "" else None

class userinfo:
    def __init__(self,username:str,password:str) -> None:
        self.username = username
        self.password = password