from abc import ABC, abstractmethod

class Pyatm(ABC):


    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")




class Amit(Pyatm):
    def payfee(self):
        print("paid")



amit = Amit()
amit.enrolled()