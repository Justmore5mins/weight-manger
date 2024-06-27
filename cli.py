from core import *
from datetime import date

COMMANDLIST = ["/login","/read","/write","/new","/update","/delete","/draw","/help","/?"]

while True:
    entered = input("> ")
    parts = entered.split(" ")
    command = parts[0]
    if command not in COMMANDLIST:
        print("read /help to know what command you can use")
    else:
        if command == "/login":
            password = parts[2]
            state:int = Mangement(parts[1],password).login()
            while state != 0:
                if state == 1:
                    print("user not exists and retype whole command again")
                if state == 2:
                    print("password might wrong")
                    password = input("please retype the password")
                    state = Mangement(parts[1],password).login()
            if state == 0:
                mange = Mangement(parts[1],password)
                print(f"Welcome {parts[1]}")
        
        if command == "/read":
            print(data for data in mange.read())
        if command == "/write":
            try:
                time = date(parts[4].split(" ")[0],parts[4].split(" ")[1],parts[4].split(" ")[2])
            except:
                time = date.today()
            mange.write(time,float(parts[1]),float(parts[2]))
        if command == "/new":
            Mangement(parts[1],parts[2]).new(float(parts[3]))
        if command == "/update":
            key, value = parts[1].split("=")
            mange.update(key=value)
        if command == "/delete":
            if input("r u serious? (Y/n)").lower() == "y":
                if input("really? (Y/n)  ").lower == "y":
                    mange.delete()
                else:
                    pass
            else:
                pass
        if command == "/draw":
            mange.draw()
        if command == "/help" or command == "/?":
            print("This is a simple code which can record your weight data")
            print(f"there are {len(COMMANDLIST)} commands, {COMMANDLIST}")
            print("the /login command is log in to the user: /login {username} {password}")
            print("the /read function can read data saved in it : /read")
            print("the /new function can create new user: /new {username} {password} {height}")
            print("the /update function updates the exists user's data: username password and height(edit one item per time):/update {target}={value}")
            print("the /delete function is delete the exists user: /delete")
            print("the /draw function uses exists data to draw the linar chart:/draw")
            print("the /help or /? shows this")