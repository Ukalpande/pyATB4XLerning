# calculater program uing constructor

class calc:
    def __init__(self):
        print("DC")

    def sum(self, a, b, c):
        return a + b + c

    def sub(self, a, b, c):
        return a - b - c

    def mul(self, a, b, c):
        return a * b * c

    def div(self, a, c):
        return a / c


output_ref = calc()
a = int(input("enter the value of a \n"))
b = int(input("enter the value of b \n"))
c = int(input("enter the value of c \n"))

op_sum = output_ref.sum(a, b, c)
op_sub = output_ref.sub(a, b, c)
op_mul = output_ref.mul(a, b, c)
op_div = output_ref.div(a, c)

print(op_sum)
print(op_sub)
print(op_mul)
print(op_div)
