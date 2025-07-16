      #  Simple function

city = ["jaipur" , "kota" , "delhi" , "chandigarh" , "Banglore"]

# def length(city):
#     return len(city)
# sort = sorted(city , key=length)
# print("Sorted word by length: ",sort)

   #  Convert before code in lambda function

sort = sorted(city , key=lambda x: len(x))     # reverse = True means decending order
print(f"Sorted word by length: {sort}")

# add_ten = lambda x : x + 10
# print(add_ten(5))

# multiply = lambda a , b : a * b
# print(multiply(5,2))

numbers = [1,2,3,4,5,6]    # using map
sqr = list(map(lambda x : x ** 2, numbers))
print(sqr)


even = list(filter(lambda x : x % 2 == 0 , numbers))     # Using filter
print(even)

pairs = [(1 , "One"),(2 , "Two") , (3 , "Three")]
sorted_pairs = sorted(pairs , key=lambda x : x[1])
print(sorted_pairs)