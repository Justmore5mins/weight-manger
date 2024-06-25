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
    
    def login(self):
        userinfo:dict = {}
        with open(self.info) as file:
            for data in file.readlines():
                userinfo["username"] = data.split(" ")[0]
                userinfo["password"] = data.split(" ")[1]
        if self.username not in userinfo.keys():
            print("the user not exists")
        else:
            

    def __check__(self):
        return isfile(f"data/{self.username}.info")