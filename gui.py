from tkinter import Tk,Label,Button,Entry

win = Tk()
win.title("Weight Manger")
ratio:int = 30
win.geometry(f"{16*ratio}x{9*ratio}")
Label(text="User",font=("JetBrains Mono",16)).pack()
user = Entry()

win.mainloop()