class Apple:
    price = 5
    

    def __init__(self, color):
        self.__color = color
        self.__price = Apple.price

    def __repr__(self):
        return "This is a %d cedi %s apple" % (self.__price, self.__color)

    @classmethod
    def change_price(cls, price):
        cls.price = price


first = Apple("red")
print(first)


second = Apple("blue")
print(second)

Apple.change_price(6)
third = Apple("green")
print(third)

print(first)

fourth = Apple("yellow")
print(fourth)

Apple.change_price(15)
fifth = Apple("purple")
print(fifth)
