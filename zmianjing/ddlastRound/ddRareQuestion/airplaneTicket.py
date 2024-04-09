'''
You're building a tool to estimate the cost of various airplane tickets based on the airline, distance and seating class.
 Your tool must take in this information as a series of inputs (one ticket calculation per line of input) and produce a list of output costs.
Each airline contains its own cost requirements. Ultimately, the airline is only interested in two major components:
 the space you take on the plane, and the distance you fly. You must generate ticket costs using this gathered data:
Airlines: United, Delta, Southwest, LuigiAir
Operating Costs:
- Economy:  No charge
- Premium:  $25
- Business: $50 + $0.25/mile
Per-Airline Prices:
- Delta charges $0.50/mile
   + OperatingCost
- United charges $0.75/mile
   + OperatingCost
   + $0.10/mile for Premium seats
- Southwest charges $1.00/mile
- LuigiAir charges $100 or 2 * OperatingCost, whichever is higher
Keep in mind that, while there are only four airlines listed above, your solution should be able to expand to dozens of
individual airlines,  whose ticket cost can be based on arbitrary functions of "Operating Costs", miles, and/or seating class.
You can assume that the input will be provided as a list of strings and that there could be millions of lines of input.
Each string will provide the Airline, Distance and Seating Class. Please review the examples below:
Example Input:
-------------------------------------------
United 150.0 Premium
Delta 60.0 Business
Southwest 1000.0 Economy
LuigiAir 50.0 Business
-------------------------------------------
Example Output:
-------------------------------------------
152.50
95.00
1000.00
125.00
-------------------------------------------
Explanation of Output:
-------------------------------------------
152.50      (150.0 * (0.75 + 0.10) + 25)
95.00       (60.0 * (0.50 + 0.25) ‍‌‍‌‍‍‍‍‌‌‌‍‌‍‌‍‌‍+ 50)
1000.00     (1000.0 * 1.00)
125.00      (100 <= 2 * (50 + 50 * 0.25))
-------------------------------------------
'''

## 这道题 反射+ oo 设计
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
        self.price_dict = {
            "United":UnitedPrice,
            "Delta":DeltaPrice,
            "Southwest":SouthwestPrice,
            "Luigi":LuigiAirPrice
        }

    #["name","miles","type"]
    def getTotalPrice(self,infos:list[list[str]]):
        if not infos or len(infos) == 0:
            return 0
        res = []
        for info in infos:
            air_name,miles,type_name = info[0],info[1],info[2]
            if air_name in self.price_dict: # belong to one of us ticket map
                cur_airline = self.price_dict[air_name]()
                ## bug 在这里。没调函数 蠢比！！
                # res.append(cur_airline(miles,type_name))
                price = cur_airline.getPrice(miles, type)
                res.append(price)
            else:
                print("error happened")
                continue
                # pass

        return res


if __name__ == "__main__":

    sampleinput = [['United', '150.0', 'Premium'],
                   ['Delta', '60', 'Business'],
                   ['Southwest', '1000.0', 'Economy'],
                   ['Luigi', '50.0', 'Business']]
    sol = solution()
    print(sol.getTotalPrice(sampleinput))
