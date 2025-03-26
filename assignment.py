my_list = []
#append 10,20,30,40 intothe list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#Insert 15 at the second position of the list
my_list.insert(1, 15)
#Extend the list with 50,60,70
my_list2 = [50,60,70]
my_list.extend(my_list2)
print(my_list)
#remove the last element from the list
my_list.pop()
#sort my list  in ascending order
my_list.sort()
#Print the index of 30in the list
index_of_30 = my_list.index(30)
print(index_of_30)


