from abc import abstractmethod

class airplaneTicket:

    @abstractmethod
    def getPrice(self,miles:int,cate:str):
        pass
    '''
    Operating Costs:
- Economy:  No charge
- Premium:  $25
- Business: $50 + $0.25/mile
    '''
    #这是一个共有的类 所以应该包在父类里
    def operatingCost(self,miles:int, cate:str):
        if cate == "E":
            return 0.0
        elif cate == "P":
            return 25.0
        elif cate == "B":
            return miles * 0.25 + 50

class United(airplaneTicket):
    def getPrice(self,miles:int,cate:str):
        pre_price = 0
        if cate == 'E':
            pre_price += 0.75 * miles
        elif cate == 'P':
            pre_price += (0.75 + 0.1) * miles
        elif cate == 'B':
            pre_price += 0.75 * miles

        return pre_price + self.operatingCost(miles,cate)

class Delta(airplaneTicket):
    def getPrice(self,miles:int,cate:str):
        pre_price = 0.5 * miles
        return pre_price + self.operatingCost(miles,cate)

class Southwest(airplaneTicket):
    def getPrice(self,miles:int,cate:str):
        return 1 * miles

class Luigi(airplaneTicket):
    def getPrice(self,miles:float,cate:str):
        op_cost = self.operatingCost(miles,cate)
        return 100 if op_cost *2 < 100 else 2*op_cost

class solution:
    def __init__(self):
        self.nameToClass = {
            'United':United,
            'Delta':Delta,
            'Southwest': Southwest,
            'Luigi': Luigi
        }
    def getAirPrice(self,infos:list[tuple]):
        if not infos or len(infos) == 0 :
            return []
        res = []
        for info in infos:
            air_name,mile,cate = info[0],info[1],info[2]
            print(air_name,mile,cate)
            if air_name in self.nameToClass:
              ## use map to get class name
                cur_airline = self.nameToClass[air_name]()
                price = cur_airline.getPrice(mile,cate)
                res.append(price)
            else:
                print(air_name)
                raise Exception("wrong input")

        return res

sampleinput = [('United', 150.0, 'P'),
               ('Delta', 60, 'B'),
               ('Southwest', 1000.0, 'E'),
               ('Luigi', 50.0, 'B')]
sol = solution()
print(sol.getAirPrice(sampleinput))