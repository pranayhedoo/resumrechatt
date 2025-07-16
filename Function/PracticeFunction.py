#   # Practise Q1

# # def myFunction():    #  create function 
  
# #   print("Welcome to python course by Pranay")

# # myFunction()  #  Call function

#  #  Practise Q2

# # def add2Number(a,b):   # parameters a b
# #   result = a + b
# #   print(f"the sum is {result}")

# # add2Number(5,3)

# #  adding return function in function

# # def addnum(a,b):
# #   return a+b
# #   return a*b   # this 2nd result are not visible
# # sum2num = addnum(5,8)
# # print(sum2num)

#     # Example for full function using return statement

# # def celsius_to_fahrenheit(celcius):
# #   fahrenheit = (celcius * 9/5) + 32
# #   return fahrenheit

# # temp_f = celsius_to_fahrenheit(25)    
# # print(temp_f)

#      # Example for full function without return statement

# def celsius_to_fahrenheit(celsius):
#     fahreheit = (celsius * 9/5) + 32
#     print(fahreheit)

# celsius_to_fahrenheit(58)   #  call function


#      # Pass statement

# def anywhere():   #  this code are right in future 
#     pass

# print("Hello")

def show_even_numbers():
    numbers = list(range(1, 21))  # Create a list of numbers from 1 to 20
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    print("Even numbers from 1 to 20:")
    print(even_numbers)

# Call the function
show_even_numbers()
