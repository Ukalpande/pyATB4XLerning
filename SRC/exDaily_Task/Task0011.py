# create a eployee class
# with the use of constructor
# Atribute = name , age  phone, address, E-id
# Biheviour = walk, talk, print, details
# with the costructor which will set the values
#ask user about the informetion for E1,E2
#print the details of the E1, E2 via print employee function.


class Employee:

    name = None
    age = None
    phone = None
    eid = None
    address = None

def __init__(self, name,age,phone,eid,address):
    self.name = name
    self.age = age
    self.phone = phone
    self.eid = eid
    self.address = address
def walk(self):
    print("emp can walk")
def talk(self):
    print("emp can talk")
    



def printdetails(self):
    print("Name of Employee is ", self.name)
    print("Age of Employee is ", self.age)
    print("phone of Employee is ", self.phone)
    print("Eid of Employee is ", self.eid)
    print("Address of Employee is ", self.address)

    name = input("Enter the name of Emp1 \n")
    age = input("Enter the age of Emp1 \n")
    phone = input("Enter the phone of Emp1 \n")
    eid = input("Enter the eid of Emp1 \n")
    address = input("Enter the address of Emp1 \n")




#emp1 = Employee("name, age, eid,phone, address \n")
#emp1.talk()
#mp1.walk()
#emp1.printdetails()


#not run error need help ,,,,,,

