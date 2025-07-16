#   #  What is tuple  It is a collection ordered unchangeable and duplicate are available

#   # create tuple in python

# my_tuple = (1,2,3)
# print(type(my_tuple))

# Fruits = ("Banana" , 1 , "Apple" , 2 , "Cherry")   # mixed tuple

#    #   using tuple constructor

# tuple2 = tuple((1,5,9))
# print(type(tuple2))

# #  Create a single element

# A = ("A",)      #  , dilya ni tuple bnte
# print(type(A))

# # Access tuple - indexing

Fruits1 = ("Banana" , "Apple" , "Cherry")

print(Fruits1[-1])      # only one printed

  #    All same as list operations

     #   Packing and unpacking tuple  

  # Packing :- putting multiple values in singl tuple

a = "Pranay"
b = 25
c = "Engineer"
tuple_pack = a,b,c
print(tuple_pack)

  #  unpacking :- it is extracting the value from a tuple into seprate

name , age , prefession = tuple_pack
print(name)
print(age)
print(prefession)