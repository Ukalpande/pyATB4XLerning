# create a eployee class
# with the use of constructor
# Atribute = name , age  phone, address, E-id
# Biheviour = walk, talk, print, details
# with the costructor which will set the values
# ask user about the informetion for E1,E2
# print the details of the E1, E2 via print employee function.


class Employee:
    def __init__(self):
        self.name = input("Enter the nmme of emp\n")
        self.age = input("Enter the age of emp\n")
        self.phone = input("Enter the phone of emp\n")
        self.eid = input("Enter the eid of emp\n")
        self.address = input("Enter the address of emp\n")

    def name_of_the_function(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"phone is {self.phone}")
        print(f"emp is {self.eid}")
        print(f"address is {self.address}")


emp1 = Employee()
emp1.name_of_the_function()

# not run error need help ,,,,,,
