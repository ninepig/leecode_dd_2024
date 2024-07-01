from abc import abstractmethod



class AirPlaneTicket:

    @abstractmethod
    def getPrice(self,miles:str,type:str):
        pass



class UnitedPrice(AirPlaneTicket):
    def getPrice(self,miles:str,type:str):
        pre_price = 0.75 * float(miles)
        if type == "Economy":
            pre_price += 0
        elif type == "Premium":
            pre_price += 0.1 * float(miles) + 25
        elif type == "Bussiness":
            pre_price += 0.25 * float(miles) + 50
        return pre_price



class DeltaPrice(AirPlaneTicket):
    def getPrice(self,miles:str,type:str):
        pre_price = 0.5 * float(miles)
        if type == "Economy":
            pre_price += 0
        elif type == "Premium":
            pre_price += 25
        elif type == "Business":
            pre_price += 0.25 * float(miles) + 50
        return pre_price


'''
opearting
- Economy:  No charge
- Premium:  $25
- Business: $50 + $0.25/mile

- Delta charges $0.50/mile
   + OperatingCost
- United charges $0.75/mile
   + OperatingCost
   + $0.10/mile for Premium seats
- Southwest charges $1.00/mile
- LuigiAir charges $100 or 2 * OperatingCost, whichever is higher
'''

class SouthwestPrice(AirPlaneTicket):
    def getPrice(self,miles:str,type:str):
        pre_price = 1 * float(miles)
        if type == "Economy":
            pre_price += 0
        elif type == "Premium":
            pre_price += 25
        elif type == "Business":
            pre_price += 0.25 * float(miles) + 50
        return pre_price

class LuigiAirPrice(AirPlaneTicket):
    def getPrice(self,miles:str,type:str):
        pre_price = 0
        if type == "Economy":
            pre_price += 0
        elif type == "Premium":
            pre_price += 25
        elif type == "Business":
            pre_price += 0.25 * float(miles) + 50
        return 100 if pre_price * 2 < 100 else pre_price*2



class solution:

    def __init__(self):
        self.airPlanceDict = {
            'United':UnitedPrice,
            'Delta':DeltaPrice,
            'Southwest':SouthwestPrice,
            'Luigi' : LuigiAirPrice
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
            price = cur_airline.getPrice(mile,type)
            res.append(price)

        return res




if __name__ == "__main__":
    sampleinput = [['United', '150.0', 'Premium'],
                   ['Delta', '60', 'Business'],
                   ['Southwest', '1000.0', 'Economy'],
                   ['Luigi', '50.0', 'Business']]
    sol = solution()
    print(sol.calcPirceFromDifferentAirline(sampleinput))