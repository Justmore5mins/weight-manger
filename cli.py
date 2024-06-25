from core import *
from datetime import date

COMMANDLIST = ["/load","/read","/write","/new","/update","/new","/delete","/draw","/help"]

while True:
    entered = input("> ")
    parts = entered.split(" ")
    command = parts[0]
    if command not in COMMANDLIST:
        print("read /help to know what command you can use")
    else:
        if command == "/login":
            user = parts[1]
            password = parts[2]
            state = Mangement(user,password).login()
            if state == 0:
                manger = Mangement(user,password)
            elif state == 1:
                print("The user exists")
            elif state == 2:
                print("the password(or user) is wrong")
            else:
                print("i remember that i haven't set this exception")

        if command == "/new":
            Mangement(parts[1]).new([float(parts[2])])
        if command == "/delete":
            if input("Are you sure about that? (Y/n) ").lower() == "y":
                if input("serious? (Y/n) ").lower() == "y":
                    manger.delete()
        if command == "/read":
            dat:list[list[str]] = []
            output:list[str] = []
            output.append("Time        User      Weight   BMI")
            output.append("----------------------------------")
            for entry in manger.read():
                data = entry.get(user)
                dat.append([data.get("time"),user,data.get("weight"),data.get("fat"),data.get("BMI")])
            for time,user,weight,fat,bmi in dat:
                output.append(f"{time}  {user+" "*(10-len(user))}{str(weight)+" "*(9-len(str(weight)))}{bmi}")
            for i in output:
                print(i)

        if command == "/write":
            time = date(int(parts[3].split("-")[0]),int(parts[3].split("-")[1]),int(parts[3].split("-")[2])) if len(parts) == 4 else date.today()
            manger.write(TIME=time,weight=float(parts[1]),fat=float(parts[2]))
        if command == "/update":
            print("modify one item a time")
            test = 0
            key,value = parts[1].split("=")
            ablelist = ["username","password","height"]
            if key not in ablelist:
                print(f"it is only support {ablelist} so far")
            else:
                manger.update(key=value)

        
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