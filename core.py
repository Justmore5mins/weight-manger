from errors import *
from os.path import isdir
from os import mkdir,walk,getcwd

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
            if not self.__check__():
                raise UserError("The user not exists")
            else:
                pass
            output:list[dict[str,dict[str,float|str]]] = []
            entries = open(self.file,"r").readlines()[1:]
            for entry in entries:
                elements = entry.split(" ")
                output.append({self.user:{"time":elements[0],"weight":elements[1],"fat":elements[2],"BMI":elements[3]}})
            return output
    
    def write(self,time:str,weight:float,fat:float):
        if not self.__check__():
            raise UserError("The user not exists")
        else:
            pass
        with open(self.file,"r") as file:
            height = float(file.readline().rstrip())
            bmi = weight/((height/100) ** 2)
        with open(self.file,"a") as file:
            file.write("\n")
            file.write(f"{time} {weight} {fat} {bmi}")

    def update(self,data:list):
        if not self.__check__():
            raise UserError("The user not exists")
        else:
            pass
        with open(self.file,"r") as file:
            lines = file.readlines()
        lines[0] = data
        for i in data:
            with open(self.file,"w") as file:
                file.write(f"{i}\n")

    def __check__(self):
        new = []
        userlist = next(walk(getcwd()))[2]
        for i in userlist:
            new.append(i[:-7])
        state = True if self.user in new else False
        return state

if __name__ == "__main__":
    data = Mangement("entry.weight").read()
    print(data)