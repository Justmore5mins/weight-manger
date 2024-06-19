from errors import *
from os.path import isdir
from os import mkdir,walk,getcwd,remove
from matplotlib import pyplot as plt
from datetime import date,datetime
from os import system #testing usage

class Mangement:
    def __init__(self,username:str,password:str) -> None:
        self.username = username
        self.password = password
        self.file = f"data/{username}.weight"
        self.userinfo = f"data/{username}.info"
        if isdir("data") and isdir("keys"):
            pass
        else:
            self.__create__(username,["data",["keys"]])
        
    def login(self):
        pass

    def new(self,Data:tuple[str,str,float]):
            """
            .info file format:
            [user] [password] [height] [salt]
            """
            if self.__check__():
                raise UserError("The user exists")
            else:
                pass
            open(self.file,"x").close()
            open(self.userinfo,"x").close()
            username,password,height = Data
            
    def delete(self):
        remove(self.file)

    def read(self):
            output:list[dict[str,dict[str,float|date]]] = []
            entries = open(self.file,"r").readlines()
            for entry in entries:
                elements = entry.split(" ")
                output.append({self.username:{"time":date(int(elements[0].split("-")[0]),int(elements[0].split("-")[1]),int(elements[0].split("-")[2])),"weight":float(elements[1]),"fat":float(elements[2]),"BMI":float(elements[3])}})

            return output

    def write(self,weight:float,fat:float,TIME:date):
        infos:dict[str,float] = []
        with open(self.file,"r") as file:
            with open(self.userinfo,"r") as data:
                for info in data.readlines():
                    user, password, height = info.split(" ")
                    infos[user] = float(height)
            bmi = weight/(infos.get(self.username) ** 2)
            data = file.readlines()
            data.append(f"{TIME} {weight} {fat} {bmi}")
        with open(self.file,"w") as file:
            if len(data) > 0:
                times:list[date] = []
                weights:list[float] = []
                fats:list[float] = []
                bmis:list[float] = []
                for i in data:
                    Ctime, Cweight, Cfat, Cbmi = i.split(" ")
                    Ctime = date(int(Ctime.split("-")[0]),int(Ctime.split("-")[1]),int(Ctime.split("-")[2]))
                    Cweight = float(Cweight)
                    Cfat = float(Cfat)
                    Cbmi = float(Cbmi)
                    times.append(Ctime)
                    weights.append(Cweight)
                    fats.append(Cfat)
                    bmis.append(Cbmi)
                file.write(f"{data[0]}")
                for i in self.__listup__(times,weights,fats,bmis):
                    time,weight,fat,bmi = i
                    file.write(f"{time} {weight} {fat} {bmi}\n")
            else:
                file.write(f"{data[0]}")
                file.write(f"\n{TIME} {weight} {fat} {bmi}")
    def update(self,**modify):
        """
        format:
        >>> {user:{want to modify:"value"}}
        """
        writing:list[str] = []
        infos:dict[str,dict[str,str|float]] = {}
        with open(self.userinfo,"r") as file:
            for data in file.readlines():
                username, password, height = data.split(" ")
                infos[username] = {"password":password,"height":float(height)}
        for key in modify.keys():
            infos[username][key] = modify[key]
        
        for user in infos:
            writing.append(f"{user} {infos[user]["password"]} {infos[user]["height"]}")
        return writing

    def draw(self):
        times:list[date] = []
        weights:list[float] = []
        fats:list[float] = []
        with open(self.file,"r") as file:
            info = file.readlines()
            for i in info:
                times.append(datetime(int(i.split(" ")[0].split("-")[0]),int(i.split(" ")[0].split("-")[1]),int(i.split(" ")[0].split("-")[2])))
                weights.append(float(i.split(" ")[1]))
                fats.append(float(i.split(" ")[2]))
        plt.plot(times,weights,"b-o")
        plt.plot(times,fats,"y-o")
        plt.xlabel("Time")
        plt.ylabel("Weight & Fat Percentage")
        plt.xlim(times[-1],times[0])
        plt.ylim((min(fats)-5),(max(weights)+5))
        plt.title("Wight & fat liner chart")
        plt.legend(["weight","fat"],loc="best")
        plt.show()

    def __create__(self,username:str,dirs:list[str]):
        mkdir(dirname for dirname in dirs)
        return username

    def __check__(self):
        new = []
        userlist = next(walk(f"{getcwd()}/data"))[2]
        for i in userlist:
            new.append(i[:-7])
        state = True if self.username in new else False
        return state

    def __listup__(self,time:list[date],weight:list[float],fat:list[float],bmi:list[float]):
        return sorted(zip(time,weight,fat,bmi))


if __name__ == "__main__":
    system("python3 cli.py")
