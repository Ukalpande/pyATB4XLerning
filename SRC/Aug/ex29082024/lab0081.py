# list
# list collection of items (duplicates is allowed )
# my_list = [1,2,3] # same type of data (int)
# my_list = [1, true, "ujwal",12,24]


my_list = [1, 2, 3, 4, 5, 6]

print(my_list)  # printing the list
print(len(my_list))  # detecting the lenth of lst

print(my_list[0])  # printing the fst number in the list (list start from 0 Always)
print(my_list[2])  # printing 2nd position number

# indexing
# changing the valuse ...

my_list[0] = "ujwal"
my_list[1] = "kalpande"
my_list[2] = "tester"
print("element at the index 0", my_list[0])
print("element at the index 0", my_list[1])
print("element at the index 0", my_list[2])

print(my_list)
for element in my_list:
    print(element)

for i in range(1, 10):  # (1,2,3,4,5,6,7,8,9)
    print(i)

# append / extend
my_list.append(7)  # append not add mltipal num at one time it add one at a time
my_list.extend([8, 9])  # EXTEND use for adding multipal element at a time
print(my_list)

# insert

my_list.insert(3, "python")
print(my_list)


#remove

my_list.remove("python")
print(my_list)

#copy

my_copy_list = my_list.copy()
#print(my_list)
print(my_copy_list)

#Clear

my_list.clear()
print(my_list)
print(my_copy_list)

#reverse

my_copy_list.reverse()
print(my_copy_list)

my_copy_list.sort(reverse=False)
print(my_copy_list)

name = "ujwal"
name = name.upper()
print(name)

