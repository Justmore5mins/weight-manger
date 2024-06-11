from errors import *
from os.path import isdir
from os import mkdir,walk,getcwd
from matplotlib import pyplot as plt
from datetime import date,datetime
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
            output:list[dict[datetime,dict[str,float|str]]] = []
            entries = open(self.file,"r").readlines()[1:]
            for entry in entries:
                elements = entry.split(" ")
                output.append({self.user:{"time":datetime.strptime(elements[0],r"%Y-%m-%d"),"weight":float(elements[1]),"fat":float(elements[2]),"BMI":float(elements[3])}})
            
            return output
    
    def write(self,weight:float,fat:float,TIME:date):
        with open(self.file,"r") as file:
            data = file.readlines()
            height = float(data[0])
            bmi = f"{int(weight/((height/100) ** 2)*100)/100}"
        with open(self.file,"w") as file:
            if len(data[1:]) > 0:
                times:list[date] = []
                weights:list[float] = []
                fats:list[float] = []
                bmis:list[float] = []
                for i in data[1:]:
                    Ctime, Cweight, Cfat, Cbmi = i.split(" ")
                    Ctime = date(int(Ctime.split("-")[0]),int(Ctime.split("-")[1]),int(Ctime.split("-")[2]))
                    Cweight = float(Cweight)
                    Cfat = float(Cfat)
                    Cbmi = float(Cbmi)
                    times.append(Ctime)
                    weights.append(Cweight)
                    fats.append(Cfat)
                    bmis.append(Cbmi)
                times.append(TIME)
                weights.append(weight)
                fats.append(fat)
                bmis.append(bmi)
                file.write(f"{data[0]}")
                for i in self.__listup__(times,weights,fats,bmis):
                    time,weight,fat,bmi = i
                    file.write(f"{time} {weight} {fat} {bmi}\n")
            else:
                file.write(f"{data[0]}")
                file.write(f"\n{TIME} {weight} {fat} {bmi}")
    def update(self,Hi:float):
        with open(self.file,"r") as file:
            data = file.readlines()
            data[0] = f"{Hi}" if data else data.append(f"{Hi}")
        with open(self.file,"w") as file:
            for i in data:
                file.write(f"{i}")
        return Hi

    def draw(self):
        times:list[date] = []
        weights:list[float] = []
        fats:list[float] = []
        with open(self.file,"r") as file:
            info = file.readlines()[1:]
            for i in info:
                times.append(datetime(int(i.split(" ")[0].split("-")[0]),int(i.split(" ")[0].split("-")[1]),int(i.split(" ")[0].split("-")[2])))
                weights.append(float(i.split(" ")[1]))
                fats.append(float(i.split(" ")[2]))
        plt.plot(times,weights,"b-o")
        plt.plot(times,fats,"y-o")
        plt.xlabel("Time")
        plt.ylabel("Data")
        plt.xlim(times[-1],times[0])
        plt.ylim((min(fats)-5),(max(weights)+5))
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
    
    def __listup__(self,time:list[date],weight:list[float],fat:list[float],bmi:list[float]):
        return sorted(zip(time,weight,fat,bmi))


if __name__ == "__main__":
    system("python3 cli.py")