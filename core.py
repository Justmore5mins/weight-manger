from errors import *

class Mangement():
    def __init__(self,path:str) -> None:
        self.file = path

    def read(self):
        """
        return type

        >>> {user(str):{time:str, weight:float, fat_percentage:float}
        """
        entries:list[dict[str,dict[str,str|float]]] = []
        with open(self.file,"r") as file:
            for line in file:
                line.strip()
                element= line.split(" ")
                if len(element) != 4:
                    SyntaxError(f"it requires 4 elements, but it has only {len(element)}.")
                else:
                    try:
                        entries.append({element[1]:{"time":element[0],"weight":element[2],"fat percentage":element[3]}})
                    except:
                        SyntaxError("Check the file format if there's something went wrong")
        return entries
    def write(self,username:str,weight:float,fat:float,time:str) -> None:
        with open(self.file,"a") as file:
            file.write("\n")
            file.write(f"{time} {username} {weight} {fat}")

if __name__ == "__main__":
    data = Mangement("entry.weight").read()
    print(data)