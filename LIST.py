List = [] #empty list in python
string_list = ["javeed", "saddu", "mr.gela", "harhsa"]
integer_list = [1,2,3,4,5]
hetero_list = [1, "javeed", 5.5] #heterogeneous group of elements

# #CRUD
# #ADDING ELEMENTS TO THE LIST
integer_list.append(6) #adding single element
print(integer_list)
# #adding multiplt elements
integer_list.extend([7, 8, 9])
print(integer_list)
# #adding a single element at specific index
integer_list.insert(1, 1.5)
print(integer_list)
# #retrieving elements from the list
print(integer_list[1])
# #retrieving all elements from the list
for i in range(len(integer_list)):
    print(integer_list[i])
#
# #updating an element in the list
# #1.5 to 1.7
integer_list[1] = 1.73 #syntax list_name[index] = value
print(integer_list)
#
#deleting operation
# integer_list.remove(1)
# print(integer_list)
# integer_list.pop(1)
# print(integer_list)
# print(integer_list.pop(2))
# print(integer_list)
# # adding list to list
# hetero_list = [1, "javeed", 5.5]
# hetero_list.extend(["ABC",integer_list])
# print(hetero_list)
# print(hetero_list[4][2])
# #access elements from nested list
# # syntax--list_name[idex of nested list][index of element in nested list]
# # print(hetero_list[5][2])
#
# #slicing operation
# print(integer_list)
# #reversing all elements in the list
# print(integer_list[::-1]) #list_name[::-1]
# print(integer_list)
# print(integer_list[1:4])
# print(integer_list[2:6])
# print(integer_list[:2])
# print(integer_list[1:])
# print(integer_list[-5:])
# print(integer_list[-5:-1])#list_name[startingindex : endingindex+1]
# integer_list.append(1)
# integer_list.append(1)
# print(integer_list)
# #syntax--list_name[starting: endingindex+1]
# integer_list.sort()
# print(integer_list)
# print(integer_list.index(1))
# print(integer_list.count(1))


# integer_list[1:3]= [4,5]
# print(integer_list)
integer_list.reverse()
print(integer_list)
integer_list.sort()
print(integer_list)








