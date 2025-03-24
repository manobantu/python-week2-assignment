my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


my_list.insert(1, 15) #inserts 15 at the second of the list

my_list.extend([50, 60, 70]) #adds the new list to my_list

my_list.pop() #removes the last item on the list

my_list.sort() #sorts the list in ascending order

print(my_list)

index_of_30 = my_list.index(30) #generates the index of 30

print("this is the index of 30 is ", index_of_30)