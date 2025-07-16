# #     #  Defn :- it is save as key and valur pair amd key is not duplicated

# #      #  Create simple dictonary

Student = {
    "name":"Pranay" ,
      "age" : 1,
      "level": "Intermidiate",
      "City" : "Nagpur"
}
print(Student)

# #     #  using dict Constructor

# # person = dict(name = "Pranay" , age = 0)
# # print(person)
# # print(type(person))

# #   #   Using list of tuple

# # person2 = dict([("name","Pranay") , ("age" , 0) , ("City","Nagpur")])
# # print(person2)
# # print(type(person2))

# #  #  Access Dictonary values

# # student = {
# #     1 : "class-X" , 
# #     "name" : "Pranay" , 
# #     "Grade" : "A"
# # }
# # print(student)
# # print(type(student))

# # print(student["name"])

# #   Key method this is show all keys

# Student = {1 : "Class-X",
#            "name" : "Pranay",
#            "Grade" : "A",
#            "City" : "Nagpur"
#            }

# print(Student.keys())

# #   Value method this is Shoe all values

# print(Student.values())

# #  items Method this is show all key-value pairs

# print(Student.items())

# #   get Method Return value of keys

# print(Student.get("name"))   #  None Show krte nsel tr print(Student.get("jokar"))

# #  Add modify and remove

# Student1 = {1 : "Class-X",
#            "name" : "Pranay",
#            "Grade" : "A",
#            "City" : "Nagpur"
#            }
 
# Student1["email"] = "pranaygedaoo06@gmail.com"     # Adding key and values
# print(Student1)

# Student1["Grade"] = "A+"      # Modify value for grade
# print(Student1)

# del Student1["Grade"]     # del method use 
# print(Student1)

  #  Using Lopps iteration 

Student1 = {1 : "Class-X",
           "name" : "Pranay",
           "Grade" : "A",
           "City" : "Nagpur"
           }

# Loop for keys

# for keys in Student1:
#     print(keys)

   #   loops through values

# for values in Student1:
#     print(Student1[values])
  
#     # loops through key and values

# for keys , values in Student1.items():
#     print(keys, values)

  # Using nested Dictonary

main_student = {"Student1" : {"name" : "Pranay" , "Age" : 25 , "Grade" : "A+"} , 
            "Student2" : {"name" : "Pranay" , "Age" : 25 , "Grade" : "A+"}
           }
print(main_student)
print(main_student["Student1"])
print(main_student["Student1"]["Age"])
