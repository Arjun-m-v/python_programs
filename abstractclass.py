from abc import ABC,abstractmethod


class Car(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def mileage(self):
        pass

class Honda(Car):
    name="Honda"
    def indicators(self):
        print("Indicating")
    def accelerate(self):
        print("accelerating")
    def mileage(age):
        print("Mileage is 30")

ob=Honda()
ob.indicators()
ob.accelerate()
ob.mileage()