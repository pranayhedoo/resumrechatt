class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def student_details(self):
        #  Hide in console from adding percentage + 2 and sobtract grade
        print(f"{self.name} is in class {self.grade - 2 }, with {self.percentage + 2}%")     

Student1 = Student("Madhav" , 11 , 96 )
student2 = Student("Kunal" , 10 , 85)

Student1.student_details()
student2.student_details()

# from abc import ABC, abstractmethod

# # Abstract base class
# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass  # No implementation here

#     # def description(self):
#     #     print("This is a shape.")  # Regular method, can have implementation

# # Concrete class
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# # Create object
# rect = Rectangle(10, 5)
# print("Area of rectangle:", rect.area())
# # rect.description()
