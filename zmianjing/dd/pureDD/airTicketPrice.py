class airLinePrice:
    # def __init__(self, name,base, encomoy, encomoy_mile, premium, premium_mile, bussiness, bussiness_mile):
    #     self.name = name
    #     self.base = base
    #     self.encomy = encomoy
    #     self.encomoy_mile = encomoy_mile
    #     self.premium = premium
    #     self.premium_mile = premium_mile
    #     self.bussiness = bussiness
    #     self.bussiness_mile = bussiness_mile
    def __init__(self,name):
        self.name = name
    @classmethod
    def countfinalPrice(self,miles,className):
        self.finalPrice = 0

## https://www.1point3acres.com/bbs/thread-1037303-1-1.html
#情况一：子类需要自动调用父类的方法：子类不重写__init__()方法，实例化子类后，会自动调用父类的__init__()的方法。
# type enum --> 0 means base 1 mean premium 2 means bussiness
## 应该利用反射来做 航空名--->类名---> 调用类方法
##https://blog.51cto.com/u_16175511/6717636
##https://www.cnblogs.com/huchong/p/7373952.html

## 反射需要类方法 也就是classmethod
## 然后getAtrribuite 来传参同时调用类方法
class United(airLinePrice):
    # def __init__(self,name,base,encomoy,encomoy_mile,premium, premium_mile,bussiness, bussiness_mile):
    #     self.name = name
    #     self.base = base
    #     self.encomy = encomoy
    #     self.encomoy_mile = encomoy_mile
    #     self.premium = premium
    #     self.premium_mile = premium_mile
    #     self.bussiness = bussiness
    #     self.bussiness_mile = bussiness_mile
    #     self.finalPrice = 0
    @classmethod
    def countfinalPrice(self,miles,type):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
        else:
            final += 50
            final += float(miles) * 0.25
        return final + float(miles) * 0.85


class Delta(airLinePrice):
    @classmethod
    def countfinalPrice(self,miles,type):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
            final += 0.1*miles
        else:
            final += 50
            final += float(miles) * 0.25
        return final + float(miles) * 0.5


class Southwest(airLinePrice):
    @classmethod
    def countfinalPrice(self,miles,type):
        final = 0
        # if type == "Enco":
        #     final += 0
        # elif type == "Prem":
        #     final += 25
        # else:
        #     final += 50
        #     final += miles *(0.25+0.1)
        return final + float(miles) * 1


class Luigi(airLinePrice):
    @classmethod
    def countfinalPrice(self,miles,type):
        final = 0
        if type == "Enco":
            final += 0
        elif type == "Prem":
            final += 25
        else:
            final += 50
            final += float(miles) * 0.25
        return  100 if 2 * final < 100 else 2*final


def main():
   sampleinput = [['United','150.0','Prem'],
                  ['Delta','60','buss'],
                  ['Southwest','1000.0', 'Enco'],
                  ['Luigi','50.0','buss']]
   res =[]
   for list in sampleinput:
       airlineName, miles, type = list[0],list[1],list[2]
       # use refect to count price and output
       class_name = airlineName
       method_name = "countfinalPrice"
       args = (miles,type)
       print(args)
       current_price = getattr(globals()[class_name],method_name)(*args)
       print(current_price)
       # if hasattr(class_name, method_name):  # 返回bool
       #     print('exist')
       #     Foo_func = getattr(class_name, method_name)  # 如果存在这个方法或者属性，就返回属性值或者方法的内存地址
       #     # 如果不存在，报错，因此要配合hasattr使用
       #     price = Foo_func(miles,type)
       #       print(price)



#
# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def func(self,type,miles):
#         print(123)
#         print(type)
#         print(miles)
#
# egg=Foo('hc',73)
# print(egg.name)   #hc
# print(egg.__dict__) #可以查看类的属性，不能查看方法   #{'name': 'hc', 'age': 73}
# print(egg.__dict__['name'])  #hc

if __name__ == "__main__":
    # egg = Foo('hc', 73)
    # print(egg.name)  # hc
    # print(egg.__dict__)  # 可以查看类的属性，不能查看方法   #{'name': 'hc', 'age': 73}
    # print(egg.__dict__['name'])  # hc
    # if hasattr(egg, 'func'):  # 返回bool
    #     Foo_func = getattr(egg, 'func')  # 如果存在这个方法或者属性，就返回属性值或者方法的内存地址
    #     # 如果不存在，报错，因此要配合hasattr使用
    #     Foo_func('123','123')  # 123
    main()