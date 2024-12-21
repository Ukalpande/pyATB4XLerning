

class Car:
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model #--for set the value in parametaraise costrutor

    def start_engine(self):
        print("starting the car with name " + self.name )
        print("starting the car with make " + self.make )
        print("starting the car with model " + self.model )

lambo = Car("lambo" , "v3", "2020")
lambo.start_engine()

alto = Car("alto", "S2", "TATA2")
alto.start_engine()