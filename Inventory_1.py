from class_2 import Product
class Inventory:
    def __init__(self):

        self.__products=[]
    def add(self,product:Product):
        if product in self.__products:
            raise ValueError(f"{product} already exists")
        self.__products.append(product)

    def find(self,name):
        for i in self.__products:
            if name in i.name:
               return i
        return None
    def by_value(self):
        by_value= sorted(self.__products,key=lambda p: p.price, reverse=True)
        return str(by_value)

    @property
    def total_value(self):
        total_value=sum(p.total_value for p in self.__products )
        return total_value
        # o=0
        # for p in self.__products:
        #     o+=  p.total_value



        return total_value
    o=0

