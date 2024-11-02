def sum_of_three_number(a=1,b=1,c=1):
    return a+b+c
#using defult value
result = sum_of_three_number()
print(result)
#giving two fo them the user value and one can remai same
result2 = sum_of_three_number(1,2)
print(result2)
#giving new values for all three variable

result1 = sum_of_three_number(a=2,b=3,c=1)
print(result1)

#changing the order of variable and giving the diffrent value for them

result3 = sum_of_three_number(c=20,a=30,b=50)
print(result3)



