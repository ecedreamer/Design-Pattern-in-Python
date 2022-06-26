"""
Facade Design Pattern:
Facade Pattern is a Structural Design Pattern which provides unified simpler interface
to complex classes, library or framework. 

Note: Although Facade layer makes easy for client code to use complex system, 
but it is considered as Not a good design pattern since it has many disadvantages over advantages.

In this example, we will assume complex system having electronics device controller and food ordering app.
It has one Facade class that has a start_process() method which simplifies the client code in the main 
to start the process ie. client code only has to call the start_process() method with Facade class object 
to start all processes of complex system. 
"""


import time


# complex class
class ElectronicDevice:

    def turn_on_lights(self):
        print("Turning lights on")
        time.sleep(1)

    def turn_on_fans(self):
        print("Turning fans on")
        time.sleep(1)


# complex class
class FoodOrdering:
    def order_breakfast(self):
        print("Ordering breakfast from hotel")
        time.sleep(1)

    def order_lunch(self):
        print("Ordering lunch hotel")
        time.sleep(1)

    def order_dinner(self):
        print("Ordering dinner from hotel")


# Facade class for simpler interface of complex system
class Facade:
    def __init__(self) -> None:
        self.electronic_devices = ElectronicDevice()
        self.food_ordering = FoodOrdering()

    def start_process(self):
        self.electronic_devices.turn_on_lights()
        self.electronic_devices.turn_on_fans()
        self.food_ordering.order_dinner()


def main():
    facade = Facade()
    facade.start_process()


if __name__ == "__main__":
    main()
