#✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 2
"""

Num=int(input("Enter the number to find  a factorial:"))
fact=1;
i=Num
while i>=1:
    fact=i*fact
    i=i-1
print(f"Factorial of {Num}! is: ",fact)
"""

#n= 0 or 1-> fact 1

num = int(input("Enter the int number"))
fact = 1
if num ==0 or num == 1:
    fact=1
    print(1)
else:
    for i in range(1,num+1,1):
        fact = fact*i
# |i|o/p|fact|
#  |1|NA|fact=1*1|fact=1
#  |2|NA|fact=1*2|fact=2
#  |3|NA|fact=2*3|fact=6
#  |4|NA|fact=6*4|fact=24
#  |5|NA|fact=24*5|fact=120
print(fact)

#using while loop

#i=1
#while(i<=num):
#    fact =fact*i
#    i= i+1
#print(fact)