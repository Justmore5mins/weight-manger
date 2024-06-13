from tkinter import Tk,Label,Button,Entry
import SideCode
from core import *

win = Tk()
win.title("Weight Manger")
ratio:int = 30
win.geometry(f"{16*ratio}x{9*ratio}")
win.resizable(False,False)
xaxis = 210
yaxis = 28

Label(win,text="User",font=("JetBrains Mono",16),fg="#e6e4dd",justify="center").place(x=xaxis,y=yaxis)
user = Entry(win,font=("JetBrains Mono",16),justify="center")
user.place(x=xaxis-83,y=yaxis+24)
Label(win,text="Password Not Available",font=("JetBrains Mono",16),fg="#e6e4dd",justify="center").place(x=xaxis-26,y=yaxis+62)
Password = Entry(win,font=("JetBrains Mono",16),show="*",justify="center")
Password.place(x=xaxis-83,y=yaxis+87)
Button(win,text="Login",font=("JetBrains Mono",16),command=SideCode.ReadInfo(user,Password),justify="center").place(x=xaxis+21,y=yaxis+125)
Button(win,text="New",font=("JetBrains Mono",16),command=SideCode.New(SideCode.username,SideCode.password)).place(x=xaxis-52,y=yaxis+125)
Label(text="new user type your height in password entry box",font=("JetBrains Mono",13)).place(x=48,y=yaxis+160)

user = SideCode.username
password = SideCode.password

print(f"The user {user} logged in")

win.mainloop()