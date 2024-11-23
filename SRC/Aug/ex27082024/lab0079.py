#def sum_three_num(a,b,c):
#return a+b+c


o= lambda a,b,c: a+b+c
print(o(a=2,b=4,c=6))

def find_odd_even(num):
    if num % 2 ==0:
        print("even")
    else:
        print("odd")


find_odd_even(6)

#using lambda

find_odd_even = lambda num: "even" if num % 2 == 0 else "odd"
print(find_odd_even(23))
