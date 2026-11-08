
class Product:

    def __init__(self,name,price,quantity=0):
        self.__name=name
        self.__quantity=quantity
        self.__price=price
        
    @property
    def total_value(self):
        return self.__total_value

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,valu):
        if valu<0:
            raise ValueError("price must be positive")
        self.__price=valu
    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    def add_stock(self,quantity_neu):
        if quantity_neu<0:
            raise ValueError ("amount must be positive")
        self.__quantity+=quantity_neu

    def sell(self,amaot):
        if amaot>self.__quantity:
            raise ValueError(f"not enough {self.__name}")
        self.__quantity-=amaot
    @property
    def  total_value(self) -> float:
       return self.__price * self.__quantity
    def __str__(self):
        return f"{self.__name}: {self.__quantity} x {self.__price} = {self.total_value}"