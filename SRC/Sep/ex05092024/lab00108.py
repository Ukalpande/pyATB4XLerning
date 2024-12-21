class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")

class Child (Parent):
    def BHK3(self):
        print("3BHK")

child_object = Child()
print(child_object.BHK2())
child_object.BHK3()


father_object = Parent()
#print(father_object.gold)
father_object.BHK2()
#father_object.BHK3() Attribute error --PARENT object has no attribute '3bhk'





