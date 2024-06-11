from core import *
from datetime import date

COMMANDLIST = ["/load","/read","/write","/new","/update","/new","/draw","/help"]

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
            dat:list[list[str]] = []
            output:list[str] = []
            output.append("Time        User      Weight   BMI")
            output.append("----------------------------------")
            for entry in manger.read():
                data = entry.get(user)
                dat.append([data.get("time"),user,data.get("weight"),data.get("fat"),data.get("BMI")])
            for time,user,weight,fat,bmi in dat:
                output.append(f"{time}  {user+" "*(10-len(user))}{weight+" "*(9-len(weight))}{bmi}")
            for i in output:
                print(i)

        if command == "/write":
            time = date(int(parts[3].split("-")[0]),int(parts[3].split("-")[1]),int(parts[3].split("-")[2])) if len(parts) == 4 else date.today()
            manger.write(TIME=time,weight=float(parts[1]),fat=float(parts[2]))
        if command == "/update":
            test = 0
            height = parts[1].split("=")[0]
            if height.lower() == "height":
                if manger.update(Hi=float(parts[1].split("=")[-1])) is None and test <= 10:
                    manger.update(Hi=float(parts[1].split("=")[-1]))
                    test += 1
                elif manger.update(Hi=float(parts[1].split("=")[-1])) is None and test == 11:
                    raise InternalError("Go GitHub write an issue and ")
            else:
                print("it is only support height so far")
        
        if command == "/draw":
            manger.draw()
        
        if command == "/help":
            help = []
            help.append("This is a simple code that can record your weight easily")
            help.append(f"there are {len(COMMANDLIST)} commmands: /load,/read,/write,/new,/update,/help")
            help.append("load function's usage: /load [user name]")
            help.append("read function: /read [user name]<-- this is the useage")
            help.append("the write function: /write [weight] [fat] [time(optional)]")
            help.append("update function is update your basic imformation /update height=[your height]")
            help.append("/new [user name] [height]")
            help.append("draw function: draw saved data into liner chart usage:/draw")
            help.append("/help <-- show this out")
            for i in help:
                print(i)