# Defin - comprehension is a conise way to create sequence like list , set , dictionary using a singl line code
# Types : List , Set , Dictionary 

# squares = [x ** 2 for x in range(1 , 6)]    # List comprehension
# print(squares) 

# sqr_set = {x **2 for x in range(1,6)}     # Set comprehension
# print(sqr_set)

# sqr_dict = {x : x**2 for x in range(1,6)}    # Dictionary comprehension
# print(sqr_dict)

# sqr_gen = (x**2 for x in range(1,6))
# print(next(sqr_gen))    # 1**1
# print(next(sqr_gen))     # 2**2 = 4

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# even_number = [num for row in matrix for num in  row if num % 2 == 0]
# print(even_number)
