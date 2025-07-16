#   #  Collection of item that are element changable and allow duplicate

#   #  Simple Lists in python

# list_name = ["red" , "yellow", "pink"]
# print(list_name[1])  #  no. wise

#   #    List using slicing

list1 = [10,20,30,40,50,60,70,80,90,100]
print(list1[2:8:2])
print(list1[::-1])   # reverse list

#    #  Modify list for ex. add , change , remove

my_list = ["apple" , "banana" , "Cherry"]      #  change element
my_list[1] = "mango"
print(my_list)

# my_list.append("red")   #  adding
# print(my_list)


#   Join lists

# list1 = [1,2,3]
# list2 = [4,5,6]


# final = list1 + list2      #  Direct 
# print(final)

# for x in list2:     # append method
#     list1.append(x)
# print(list1)

# list1.extend(list2)   # extend method
# print(list1)

  #   liost comprehension

  #  Create a list of square

# square = [x**2 for x in range(1,6)]
# print(square)

   #  Filter a even number 

# even_list = [x for x in range(1,10) if x % 2 ==0]
# print(even_list)

   #  apply function to each element of a list

my_list = ["Pranay" , "Hemant" , "Shakil"]

# my_name = "Pranay"
# print(my_name.upper())

# uppercase_list = [lst.upper() for lst in my_list]
# print(uppercase_list)

   #   flatten a nested list using list comp

nested_list = [[1,2],[1,2],[1,2]]
result = [item for sublist in nested_list for item in sublist]
print(result)


def flatten_list(list):
  return[item for sublist in list for item in sublist]
 
final_list = flatten_list(nested_list)
print(final_list)
