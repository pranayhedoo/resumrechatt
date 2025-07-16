# class Student:
#     def __init__(self,name,grade,percentage):
#         self.name = name
#         self.grade = grade
#         self.__percentage = percentage    #  double underscore limit access

#   #  access private body
#     def get_percantage(self):
#         return self.__percentage     # return function are required

#     def student_details(self):
#         print(f"{self.name} is in class {self.grade}, with {self.get_percantage()}%")

# Student1 = Student("Madhav" , 11 , 96)
# student2 = Student("Kunal" , 10 , 85)

# student2.student_details()
# print(Student1.get_percantage())
# print(student2.get_percantage())
# print(student2.name)

class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage  # double underscore limit access
                                                        # access private body
    def get_percantage(self):
        return self.__percentage   # return function are required
    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.get_percantage()}%")
Student1 = Student("Madhav" , 11 , 96)
student2 = Student("Kunal" , 10 , 85)
                                              # Student1.student_details()
student2.student_details()
print(Student1.get_percantage())
print(student2.get_percantage())
print(student2.name)