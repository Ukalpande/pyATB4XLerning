"""
SINGLE INHERITANCE

"""


class Father:
    key = "2bhk"

    def car(self):
        print("father car!!", "ALTO", self.key)


class Son(Father):
    key2 = "3bhk"

    def home(self):
        print("3bhk")
    def bus(self):
        print("bus")


father_object = Father()
father_object.car()


son_object = Son()
son_object.bus()
son_object.home()