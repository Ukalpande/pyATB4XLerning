from abc import ABC, abstractmethod

class GearBox(ABC):

    @abstractmethod
    def setgear(self):
        pass
class Engine:

    @abstractmethod

    def start(self):
        pass

    @abstractmethod

    def stop(self):
        pass


class Car(Engine):
    def start(self):
        print("starting the car")

    def stop(self):
        print("stop the car")

    def setgear(self):
        print("gear box ready ")

    def drive(self):
        self.start()
        self.setgear()
        self.stop()


car = Car()

car.drive()