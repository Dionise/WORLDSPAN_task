# Fix the car factory!
from abc import ABC, abstractmethod


class Car(ABC):
    """
    Car abstract class.
    """
    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def set_color(self):
        pass


class CarFactory(Car):
    """
    A car factory
    """

    def __init__(self, color: str):
        self.__color = color

    # Implement the missing abstract method get_color

    def get_color(self):
        print(f"Car color is: {self.__color}")
        
    # This method (set_color) needs the following:
    # The correct decorator adding.
    # The cls class parameter annotation needs correcting, it is wrong.
    # The return needs amending to return the instance of cls
    @classmethod
    def set_color(cls, color: str):
        return cls(color)  # Change this to return the instance of cls.


if __name__ == "__main__":
    car1 = CarFactory.set_color("red")
    car2 = CarFactory.set_color("blue")

    car1.get_color()
    car2.get_color()
