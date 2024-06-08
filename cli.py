from core import *
from datetime import date

COMMANDLIST = ["/load","/read","/write","/new","/update","/new","/help"]

while True:
    entered = input("> ")
    parts = entered.split(" ")
    command = parts[0]
    if command not in COMMANDLIST:
        print("read /help to know what command you can use")
    else:
        if command == "/load":
            user = parts[1]
            manger = Mangement(user) if Mangement(user).__check__() else print("The user not exists")

        if command == "/new":
            Mangement(parts[1]).new([float(parts[2])])
        if command == "/read":
            output:list[str] = []
            output.append("Time        User        weight     fat     BMI")
            output.append("----------------------------------------------")
            for entry in manger.read():
                data = entry.get(user)
                output.append(f"{data.get("time")}  {user}      {data.get("weight")}      {data.get("fat")}      {data.get("BMI")}")
            for i in output:
                print(i)
        if command == "/write":
            try:
                time = parts[3]
            except:
                time = date.today()
            manger.write(time=time,weight=float(parts[1]),fat=float(parts[2]))
        if command == "/update":
            key,value = parts[1].split("=")
            if key.lower() == "height":
                manger.update([value])
            else:
                print("it is only support height so far")
        
        if command == "/help":
            help = []
            help.append("This is a simple code that can record your weight easily")
            help.append(f"there are {len(COMMANDLIST)} commmands: /load,/read,/write,/new,/update,/help")
            help.append("load function's usage: /load [user name]")
            help.append("read function: /read [user name]<-- this is the useage")
            help.append("the write function: /write [weight] [fat] [time(optional)]")
            help.append("update function is update your basic imformation /update height=[your height]")
            help.append("/new [user name] [height]")
            help.append("/help <-- show this out")
            for i in help:
                print(i)