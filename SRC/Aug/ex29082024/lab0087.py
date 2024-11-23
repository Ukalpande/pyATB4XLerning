
t = ("TheTestingAcademy", "for", "TheTestingAcademy" )
print(t)
print(set(t))

#union
set = {1,2,3,4,5,6}
set1 = {7,8}
my_set = set.union(set1)
print(my_set)

#intersection
set = {1,2,3,4,5,6}
set1 = {4,5,3,7,8}
my_set = set.intersection(set1)
print(my_set)

#differance


set = {1,2,3,4,5,6}
set1 = {2,4,6,7,8,9}
my_set = set1.difference(set)
print(my_set)


# subset-- it is also use in autometion


set = {1,2,3,4,5,6}
set1 = {2,3,8}
my_set = set1.issubset(set) # check evry element is present then give true otherwise false
print(my_set)



# union -- all the element unit the diffrent element in one
#intersection--- comman element- show only comman element
#diffrance --- not comman element