# #   # Defn  :- It is a collection of unique element and do not allow duplication 

# # my_set = {1,2,3}
# # print(my_set)
# # print(type(my_set))

# #    #  create set using set constructor 

# # my_set2 = set([4,5,6])
# # print(my_set2)

# # #   Adding element 

# # number = {1,2,3,4}
# # number.add(100)
# # print(number)

# #    # Remove element 

# # Fruits = {"apple","banana"}
# # Fruits.remove("apple")
# # print(Fruits)

#    #   Methods

#    # 1. Union

Set_A = {1,2,3,4,5}
set_B = {4,5,6,7,7}
Union_Set = Set_A.union(set_B)
print(Union_Set) 

#   #  2. Intersection

# Set_A = {1,2,3,4,5}
# set_B = {4,5,6,7,7}
# Intersection_set = Set_A.intersection(set_B)
# print(Intersection_set)

# #   Set iteration

# number = {1,2,3,4,5}

# for i in number:
#     print(i)

#  Set comphrence

Square = {x**2 for x in range(1,6)}
print(Square)

count = 1
while count <= 10:
 print(count)
 count += 1