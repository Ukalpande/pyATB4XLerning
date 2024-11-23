# oop part 2

# how to take a input and create a class

class person:
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.dob = input("Enter the dob\n")

    def Display_info(self):
        print(f"Name is {self.name}")
        print(f"age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Dob is {self.dob}")


person1 = person()
person1.Display_info()
