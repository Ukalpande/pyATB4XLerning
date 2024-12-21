"""


Hybrid Inheritance


multiple types of inheritance
such as single
multiple and multilevel inheritance
"""

class A: # Father

    def methodA(self):
        return "Method A"

class B(A): #son1

    def methodB(self):
        return "Method B"
class C(A): #son2
    def methodC(self):
        return "Method C"

class D(B, C): #dother # multiple, multilevel,- MRO (method resolution order - first
    def methodD(self):
        return "Method D"

d = D()
print(d.methodD())
print(d.methodA())
print(d.methodB())
print(d.methodC())