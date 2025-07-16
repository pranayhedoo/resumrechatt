#   #  What is file handling  :- allows you to read and write to files

#   #  mode  :  r - read , w - write , a - append

#   # open a file -:  To perfoem any operation ona file.       open()

# file = open("File Handling\example.txt","r")

#      #  Syntax  -: file_object = open("file name" , "mode")

#   #  read line :- once a file is open  read , readline , readlines

# # file = open("File Handling\example.txt","r")   # File open
# # content = file.read()        # same line wise
# # #content = file.readline()    # read entire data !st line
# # #content = file.readlines()   # read file in list []
# # print(content)
# # file.close

# #   W mode   write to a line

# file = open("File Handling/example2.txt", "w")     # create a file
# file.write("Good Morning ")                              # Write contents
# file.close

# #  Append mode (Adding values)

# file = open("File Handling/example2.txt", "a")
# file.write("\n Good Afternoon")
# file.close

# # Using a context manager to open and read a file
# with open("File Handling/example.txt", "r") as file:
#     content = file.read()
#     print(content)
# # File is automatically closed here

with open("File handling/example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

    # Analyze content
    lines = content.splitlines()
    words = content.split()
    characters = len(content)

    print("\n--- File Analysis ---")
    print(f"Total Lines: {len(lines)}")
    print(f"Total Words: {len(words)}")
    print(f"Total Characters: {characters}")
