t = tuple()
print(t)


#covertion list to tuple

t1 = tuple (["ujwal", "pramod", "gopi"])
print(t1)

hero1 = ("shaktiman", "krish", "aryman")
hero2 = ("mukesh" "ritik", "shahid")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][0])
print(new_tuple[1][1])

#search in Tuple
cities = ("pune", "Mumbai", "Nagpur")
print("Akola" in cities)
print("Nagpur" in cities)

#append -- tuple object has no attribute append
# if need convert tuple in list use append in that and covert that list again in tuple

t= (12,34,56)
my_list =list(t) # tuple to list covertion
my_list.append(4) # use append in list
t= tuple(my_list) # list to tuple covertion
print(t) 

