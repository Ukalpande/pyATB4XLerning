#How to use super function


class Grandfather:
    x = 20
    def home(self):
        print("Old home")
# how father class access grandfather class function or veriable using super
class Father(Grandfather):
    a=10
    def home(self):
        print("1bhk")
        print(self.a) # calling father variable by using self
        print(super().x) # calling grandfathers variable using super
class Son(Father):
    def home(self):
        super().home() #-->(caling the parent class behavior by using super keyword ) calling super class function
        print(super().a) # also access parent class atributes by using super class
        print("NO House")


#self -- me
#super -- parent, father , super class
# super can be use within the class

ujwal = Son()
ujwal.home()
print(ujwal.x)