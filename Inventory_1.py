
class Inventory:
    def __init__(self):

        self.__products=[]
    def add(self,product):
        if product in self.__products:
            raise ValueError(f"{product} already exists")
        self.__products.append(product)

    def find(self,product):
        if product in self.__products:
            return "f{product} in the products "
        return None
    def by_value(self):
        by_value= sorted (self.__products,reverse=True)
        for i in by_value:
            print(i)



