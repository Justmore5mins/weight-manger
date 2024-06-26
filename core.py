from ast import Bytes
from torch import Value
from errors import *
from os.path import isdir,isfile
from os import mkdir,walk,getcwd,remove
from matplotlib import pyplot as plt
from datetime import date,datetime
from os import system #testing usage
from Encrypt import EasyEncrypt,AdavancedEncryption
from SideCode import userinfo

class Mangement:
    def __init__(self,username:str,password:str) -> None:
        self.username = username
        self.password = password
        self.file = f"data/{username}.weight"
        self.keys = (f"keys/{username}pub.pem",f"keys/{username}pri.pem")
        self.info = f"data/global.info"

    def new(self,height:float):
        if not isfile(self.file):
            open(self.file,"x").close()
            open(self.info,"x").close() if not isfile(self.info) else None
            with open(self.info,"a") as file:
                file.write(f"{self.username} {EasyEncrypt(self.password).encrypt()} {height} \n")
            AdavancedEncryption(userinfo(self.username,self.password)).new()
        else:
            print("The user exists")
    
    def delete(self):
        remove(self.file)
        pub, pri = self.keys
        remove(pub)
        remove(pri)
        with open(self.info,"r") as read:
            data = read.readlines()
        with open(self.info,"r") as write:
            for number,line in enumerate(data):
                if number not in data.index(self.username):
                    write.writelines(line)

    def login(self):
        userinfo:dict = {}
        usernames:list = []
        passwords:list = []
        with open(self.info) as file:
            for data in file.readlines():
                usernames.append(data.split(" ")[0])
                passwords.append(data.split(" ")[1])
                userinfo["username"] = usernames
                usernames["password"] = passwords
        if self.username not in userinfo.get("username"):
            return int(1)
        
        else:
            items = dict(zip(usernames,passwords))
            password = EasyEncrypt(items.get(self.username)).decrypt()
            state:int = 0 if self.password == password else 2
            self.height = float(data.split(" ")[2])
            return state
                
    def write(self,time:date,weight:float,fat:float):
        Times:list[date] = []
        Weights:list[float] = []
        Fats:list[float] = []
        Bmis:list[float] = []
        with open(self.file,"r") as file:
            for info in file.readlines():
                Time, Weight, Fat, Bmi = info.split(" ")
                Times.append(date(int(Time.split(" ")[0])),int(Time.split(" ")[1]),int(Time.split(" ")[2]))
                Weights.append(Weight)
                Fats.append(Fat)
                Bmis.append(Bmi)
        Times.append(time)
        Weights.append(weight)
        Fats.append(fat)
        Bmis.append((weight/(self.height ** 2)))
        with open(self.file,"w") as file:
            file.writelines(AdavancedEncryption(userinfo(self.username,self.password)).encrypt(self.__listup__(Times,Weights,Fats,Bmis,True)))
    
    def read(self):
        with open(self.file,"r") as file:
            for data in file.readlines():
                print(data)
    
    def update(self,username:str,**data):
        """
        **data support data types:
        username:str
        password:str
        height:float
        """
        with open(self.info,"r") as file:
            raw = file.readlines()
        for info in raw:
            if info.split(" ")[0] == username:
                for new in data.keys():
                    if new == "username":
                        info.split(" ")[0] = data.get("username")
                    elif new == "password":
                        info.split(" ")[1] = EasyEncrypt(data.get("password"))
                    elif new == "height":
                        info.split(" ")[2] = data.get("height")
                    else:
                        raise ValueError("Data type not supported]")
        with open(self.info,"w") as file:
            file.writelines(info)
    def __listup__(times:list[date],weights:list[float], fats:list[float], bmis:list[float],isByte:bool) -> list[str]:
        returning:list[str] = []
        Sorted = sorted(zip(times,weights,fats,bmis))
        for item in Sorted:
            time,weight,fat,bmi = item
            if isByte:
                time = bytes(time.strftime(r"%Y-%M-%d"),"utf-8")
                weight = bytes(str(weight),"utf-8")
                fat = bytes(str(fat),"utf-8")
                bmi = bytes(str(bmi),"utf-8")
            returning.append(f"{time} {weight} {fat} {bmi}")
        return returning

    def __check__(self):
        return isfile(f"data/{self.username}.info")