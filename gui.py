from tkinter import Tk,Label,Button,Entry
import SideCode

win = Tk()
win.title("Weight Manger")
ratio:int = 30
win.geometry(f"{16*ratio}x{9*ratio}")
win.resizable(False,False)
xaxis = 215
yaxis = 45

Label(win,text="User",font=("JetBrains Mono",16),fg="#e6e4dd",justify="center").place(x=xaxis,y=yaxis)
user = Entry(win,font=("JetBrains Mono",16),justify="center")
user.place(x=xaxis-83,y=yaxis+24)
Label(win,text="Password",font=("JetBrains Mono",16),fg="#e6e4dd",justify="center").place(x=xaxis-26,y=yaxis+62)
Password = Entry(win,font=("JetBrains Mono",16),show="*",justify="center")
Password.place(x=xaxis-83,y=yaxis+87)
Button(win,text="Login",font=("JetBrains Mono",16),command=SideCode.ReadInfo(user,Password),justify="center").place(x=xaxis-24,y=yaxis+125)

user = SideCode.username
password = SideCode.password
win.mainloop()