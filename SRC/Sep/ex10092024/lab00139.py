# Exception in a class



class XYZ:
    def f1(self):
        try:
            a = int(input("enter the number\n"))
        except Exception as e:
            print("Enter int only for value of a")
        else:
            print(a)
        finally:
            print("FAINALLY : ANY ONE I will be printed")

x = XYZ()
x.f1()