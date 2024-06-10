from errors import *
from os.path import isdir
from os import mkdir,walk,getcwd
from math import floor
from matplotlib import pyplot as plt
from datetime import datetime
from bisect import bisect_left
from os import system

class Mangement:
    def __init__(self,user:str) -> None:
        self.user = user if isdir("data") is True else self.__create__(user)
        self.file = f"data/{user}.weight"

    def __create__(self,username:str):
        mkdir("data")
        self.user = username

    def new(self,Data:list[str]):
            if self.__check__():
                raise UserError("The user exists")
            else:
                pass
            writing = ""
            open(self.file,"x").close()
            with open(self.file,"w") as file:
                for data in Data:
                    writing += f"{data} "
                file.write(writing)
    
    def read(self):
            output:list[dict[str,dict[str,float|str]]] = []
            entries = open(self.file,"r").readlines()[1:]
            for entry in entries:
                elements = entry.split(" ")
                output.append({self.user:{"time":elements[0],"weight":elements[1],"fat":elements[2],"BMI":elements[3]}})
            return output
    
    def write(self,weight:float,fat:float,TIME:str):
        with open(self.file,"r") as file:
            data = file.readlines()
            height = float(data[0])
            bmi = f"{int(weight/((height/100) ** 2)*100)/100}"
        with open(self.file,"a") as file:
            file.write(f"{TIME} {weight} {fat} {bmi}\n")
    def update(self,Hi:float):
        with open(self.file,"r") as file:
            data = file.readlines()
            data[0] = f"{Hi}" if data else data.append(f"{Hi}")
        with open(self.file,"w") as file:
            for i in data:
                file.write(f"{i}")
        return Hi

    def draw(self):
        weight = []
        fat = []
        time:list[datetime] = []
        for i in self.read():
            i.get(self.user)
            weight.append(float(i.get(self.user).get("weight")))
            fat.append(float(i.get(self.user).get("fat")))
            time.append(i.get(self.user).get("time"))
        plt.plot(time,weight,"b-o")
        plt.plot(time,fat,"y-o")
        plt.xlabel("Time")
        plt.ylabel("Data")
        plt.xlim(time[-1],time[0])
        plt.ylim((min(fat)-5),(max(weight)+5))
        plt.title("Wight & fat liner chart")
        plt.legend(["weight","fat"],loc="best")
        plt.show()



    def __check__(self):
        new = []
        userlist = next(walk(f"{getcwd()}/data"))[2]
        for i in userlist:
            new.append(i[:-7])
        state = True if self.user in new else False
        return state

if __name__ == "__main__":
    system("python3 cli.py")