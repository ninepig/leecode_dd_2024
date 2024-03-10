from abc import abstractmethod


class airPlanePrice:
    @abstractmethod
    def getPrice(self,miles:int, type:str):
        pass
    

class unitedState(airPlanePrice):

    def getPrice(self,miles:int, type:str):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
        else:
            final += 50
            final += float(miles) * 0.25
        return final + float(miles) * 0.85

class Delta(airPlanePrice):
    def getPrice(self, miles: int, type: str):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
            final += 0.1 * miles
        else:
            final += 50
            final += float(miles) * 0.25
        return final + float(miles) * 0.5

class SouthWest(airPlanePrice):
    def getPrice(self, miles: int, type: str):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
        else:
            final += 50
            final += miles *(0.25+0.1)
        return final + float(miles) * 1

class Luigi(airPlanePrice):
    def getPrice(self, miles: int, type: str):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
        else:
            final += 50
            final += float(miles) * 0.25
        return  100 if 2 * final < 100 else 2*final


class solution:

    def __init__(self):
        self.airPlanceDict = {
            'United':unitedState,
            'Delta':Delta,
            'Southwest':SouthWest,
            'Luigi' : Luigi
        }
    '''
    ## https://www.1point3acres.com/bbs/thread-1037303-1-1.html
    PYTHON 不需要用反射， 用抽象类 + dict[xx]() 就可以生成对应类
    '''
    def calcPirceFromDifferentAirline(self,infos:list[list[str]]):
        res = []
        for info in infos:
            airLineName , mile , type = info[0],info[1],info[2]
            cur_airline = self.airPlanceDict[airLineName]() ## way to create object with object name
            price = cur_airline.getPrice(int(mile),type)
            res.append(price)

        return res