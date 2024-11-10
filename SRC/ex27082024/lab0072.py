


my_shoping_list = ["milk", "bread", "butter"]
print(my_shoping_list[1])
print(len(my_shoping_list))


def bring_more_food(my_shoping_list):
    #user input
    more_item = input("enter the item\n") #user input
    my_shoping_list.append(more_item)
    #my_shoping_list.remove("bread")
    # use for remove perticular item from list
    my_shoping_list.insert(2, "sugar")
    # insret new item at the sertain position
    print(len(my_shoping_list))
    return my_shoping_list


l = bring_more_food(my_shoping_list)
print(l)