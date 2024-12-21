

"""
if father calss has private veriable it can be accessabe to son ..
--ans-- yes

.

"""
#Ex...>>>


class Father:
    key = "ABC"
    __password = "private"

    def __show_password(self):
        print(self.__password)


    def Father_money(self):
        return 5


    def home(self):
        return "my fathers home"


    def show_everything(self):
        self.__show_password()


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
print(s.key)
s.show_everything()
