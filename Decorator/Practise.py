# def decortor(func):
#     def wrapper():
#         print("Transaction initiated")
#         func()
#         print("Transaction completed")
#     return wrapper
    
# @decortor
# def hello():
#     print("....Executed all step in transaction.....")
# hello()

import time

def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        print("Starting function...")
        func()
        end_time = time.time()
        print("Function completed.")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)
    print("Finished processing...")

slow_function()

# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         print(f"Arguments: args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Returned: {result}")
#         return result
#     return wrapper

# @logger
# def add(a, b):
#     return a + b

# @logger
# def greet(name, message="Hello"):
#     return f"{name}, {message}!"

# # Using the decorated functions
# add(5, 3)
# greet("Heyy Jos", message="Good morning")
