# #    It is defin as one datatype to another type.

# a = "1"
# c = 2
# b = int(a)
# print(c+int(a))

# myNum = 26
# myNum2 = str(myNum)
# print(type(myNum2))

# #  Implicit type Casting
#    # Implicit is perform machine and explicit is manually
# var1 = 10
# var2 = 10.25
# var3 = var1+var2
# print(var3)
# print(type(var3))

# Using a context manager to open and read a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
