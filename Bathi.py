
class Person:

    def __init__(self, name):
        self.name = name


class Driver(Person):
    pass


class Child(Person):
    pass


class SchoolBus:

    def __init__(self, drivers=[], children=[]):
        self.drivers = drivers
        self.children = children

    def add_driver(self, driver):
        if isinstance(driver, Driver):
            self.drivers.append(driver)
        else:
            print("Get out co-driver!")

    def add_child(self, child):
        self.children.append(child)

    def drive_bus(self):
        if len(self.drivers) == 1 and len(self.children) == 10:
            print("Bus can be driven")
        else:
            print("Bus can't drive")

if __name__ == '__main__':
    import random
    newbus = SchoolBus()
    newbus.add_driver(Driver("Nana"))
for values in range(10):
    kid = input("Enter the child's name: ")
    newbus.add_child(Child(kid))

newbus.drive_bus()
