    # This 4 types of Function arguments

# 1. Required Argument
# 2. Default Argument 
# 3. Keyword Argument 
# 4. Arbitary Argument

#  1st Required Argument

def Greetings(name):  # Single name parameter
    print("Hello",name, "! ")

# Greetings("Pranay")

# def Intro(course_name , instructor_name):   # Multiple name parameter
#      print("Welcome to",course_name,"course by",instructor_name)

# Intro("Pyhton","Pranay")

    # 2 Default Argument

# def Greeting(name = "World"):    # Default values
#     print("Hello ",name ,"!")

# Greeting()

  # 3. Keyward Argument (named Argument)

# def divide(a,b):
#     return a/b
# # result = divide(100,20)
# # print(result)

# result = divide(b = 100, a = 50)
# print( result)

   # 4. Arbitary Argument
     # i Arbitary positional arguments

# def add3numbers(a,b,c):
#     return a+b-c

# result = add3numbers(15,25,21)
# print(result)

    #  Arbitary positional ch shorts

# def add_numbers(*args):
#     return sum(args)

# op =add_numbers(1,8)
# print(op)
   
   # ii Arbitary Keyward Arguments (**kwargs)  Unlimites values

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name = "Madhav", age = 25, city = "Delhi")

