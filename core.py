from errors import *
from os.path import isdir
from os import mkdir

class Mangement:
    def __init__(self,user:str) -> None:
        self.user = user if isdir("data") is True else self.__create__(user)
        self.file = f"data/{user}.weight"

    def __create__(self,username:str):
        mkdir("data")
        self.user = username

    def new(self,*data):
        writing = ""
        open(self.file,"x").close()
        with open(self.file,"a") as file:
            for i in data:
                writing += f"{i} "
            file.write(writing)
    
    def read(self):
            output:list[dict[str,str|float]] = []
            with open(self.file,"r") as file:
                entries = file.readlines()
                entries.remove(0)
            for entry in entries:
                elements = entry.split(" ")
                output.append({self.user:{"time":elements[0],"weight":elements[1],"fat":elements[2],"BMI":elements[3]}})
            return output
    
    def write(self,time:str,weight:float,fat:float):
        with open(self.file,"r") as file:
            height = float(file.readline().rstrip())
            bmi = weight/(height ** 2)
        with open(self.file,"a") as file:
            file.write("\n")
            file.write(f"{time} {weight} {fat} {bmi}")

    def update(self,data:list):
        with open(self.file,"r") as file:
            lines = file.readlines()
        lines[0] = data
        with open(self.file,"w") as file:
            file.writelines(lines)
if __name__ == "__main__":
    data = Mangement("entry.weight").read()
    print(data)