"""

multilevel Inheritance

"""

class GrandFather:
    gold = "2kg"
    def bhk1(self):
        print("1bhk")


class Father(GrandFather):
    dimond = "22karat"
    def bhk2(self):
        print("2bhk")


class Son(Father):
    btc = "1btc"

    def bhk3(self):
        print("3bhk")

#son can access grandfather , father and his attribute also
s = Son()
print(s.btc)
s.bhk3()
print(s.dimond)
s.bhk2()
print(s.gold)
s.bhk1()

#father can acccess both grand father and his attributes
f = Father()
print(f.dimond)
print(f.gold)
s.bhk2()
#Grand father can access only there attributes
g = GrandFather()
print(g.gold)
g.bhk1()

