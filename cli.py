from core import *
from datetime import date

COMMANDLIST = ["/load","/read","/write","/new","/update","/help"]

while True:
    entered = input("> ")
    parts = entered.split(" ")
    command = parts[0]
    if command not in COMMANDLIST:
        pass
    else:
        if command == "/load":
            user = parts[1]
            mange = Mangement(user)
        if command == "/read":
            output:list[str] = []
            output.append("Time        User        weight     fat     BMI")
            output.append("----------------------------------------------")
            for entry in mange.read():
                data = entry.get(user)
                output.append(f"{data.get("time")}  {user}  {data.get("weight")}  {data.get("fat")}  {data.get("BMI")}")
            for i in output:
                print(i)
        if command == "/write":
            try:
                time = parts[3]
            except:
                time = date.today()
            mange.write(time=time,weight=parts[1],fat=parts[2])
        if command == "/update":
            key,value = parts[1].split("=")
            
        
        if command == "/help":
            help = []
            help.append("This is a simple code that can record your weight easily")
            help.append(f"there are {len(COMMANDLIST)} commmands: /load,/read,/write,/new,/update,/help")