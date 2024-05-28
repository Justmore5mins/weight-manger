from core import *
from datetime import date

while True:
    COMMANDLIST = ["/load","/read","/write","/help"]
    entered = input("> ")
    parts = entered.split(" ")
    command = parts[0]
    if command not in COMMANDLIST:
        pass
    else:
        if command == "/load":
            file = parts[1]
            if file.split(".")[-1] != "weight":
                print("The file extention should be .weight")
            else:
                pass
        if command == "/read":
            user = parts[1]
            output:list[str] = []
            entires = Mangement(file).read() 
            output.append("Time        User        weight     fat")
            output.append("----------------------------------------")
            for entry in entires:
                data = entry.get(user)
                if data:
                    output.append(f"{data.get('time')}  {user}  {  data.get('weight')}kg  {data.get('fat percentage', 'N/A')}")
                else:
                    pass
            for line in output:
                print(line)
        if command == "/write":
            user = parts[1]
            weight = float(parts[2])
            fat = float(parts[3])
            try:
                time = parts[4]
            except:
                time = str(date.today())
            Mangement(file).write(user,weight,fat,time)
            
        if command == "/help":
            help = []
            help.append("This is a code which can record your body mass changes")
            help.append("It has 4 commands so far: /load /read /write /help <- you're at here")
            help.append("The /load command is loading the files(*.weight) into memory")
            help.append("*usage /load [file]")
            help.append("The /write command is write your body content")
            help.append("*usage: /write [user] [weight] [fat percentage] [time(optional)]")
            help.append("The /read command can read the entrires of a user")
            help.append("*usage: /read [user]")