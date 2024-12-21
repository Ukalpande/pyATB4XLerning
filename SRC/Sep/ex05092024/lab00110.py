"""
Multiple inheritance


"""

class Father:
    def Father_money(self):
        return 5

    def home(self):
        return "my fathers home"

class Mother:

    def Mother_money(self):
        return 10

    def home(self):
        return "My mothers home"

class Son(Mother, Father):
    pass

s = Son()
s.Mother_money()
s.Father_money()
print(s.Father_money())
print(s.Mother_money())

s.home()
print(s.home())


class Son2(Father, Mother):

    pass

s2 = Son2()
s2.home()
print(s2.home())

