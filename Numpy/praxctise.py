# import numpy as np

# height = [150,160,165,155,170]

# height_array = np.array(height)

# mean_height = np.mean(height_array)
# max_height = np.max(height_array)
# min_height = np.min(height_array)
# sorted_height = np.sort(height_array)
# total_height = np.sum(height_array)
# Std_deviation = np.std(height_array)

# print("Mean Height: ",mean_height)
# print("Maximun Height: ",max_height)
# print("Minimun Height: ",min_height)
# print("Sorted Height: ",sorted_height)
# print("Total marks: ",total_height)
# print("Standard Deviation",Std_deviation)

# import numpy as np

# # Create two 2D arrays (matrices)
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# print("Matrix A:\n", A)
# print("Matrix B:\n", B)

# # Matrix addition
# C = A + B
# print("A + B:\n", C)

# # Matrix multiplication (dot product)
# D = np.dot(A, B)
# print("A dot B:\n", D)

# # Transpose of a matrix
# A_T = A.T
# print("Transpose of A:\n", A_T)

# # Determinant of A
# det_A = np.linalg.det(A)
# print("Determinant of A:", det_A)

# import numpy as np

# # Create a NumPy array
# a = np.array([1, 2, 3, 4, 5])
# print("Original array:", a)

# # Element-wise operations
# b = a * 2
# print("Array after multiplication by 2:", b)

# # Create another array
# c = np.array([5, 4, 3, 2, 1])
# print("Second array:", c)

# # Add the two arrays
# d = a + c
# print("Sum of arrays:", d)

# # Compute mean and standard deviation
# print("Mean of d:", np.mean(d))
# print("Standard deviation of d:", np.std(d))

# # Reshape a 1D array into a 2D array
# reshaped = d.reshape((1, 5))
# print("Reshaped array (1x5):", reshaped)

# import numpy as np

# # Generate random temperature data (in Celsius) for 7 days, 4 readings per day
# temps = np.random.uniform(low=15.0, high=35.0, size=(7, 4))  # shape: (7 days, 4 readings)
# print("Temperature Data (°C):\n", np.round(temps, 2))

# # Average temperature per day
# daily_avg = np.mean(temps, axis=1)
# print("\nDaily Average Temperatures (°C):\n", np.round(daily_avg, 2))

# # Find days where average temperature exceeded 30°C
# hot_days = daily_avg > 30
# print("\nHot Days (Avg > 30°C):\n", hot_days)

# # Extract temperatures only from hot days
# hot_day_temps = temps[hot_days]
# print("\nTemperatures on Hot Days:\n", np.round(hot_day_temps, 2))

# # Max temperature of the week
# max_temp = np.max(temps)
# print("\nMaximum Temperature of the Week (°C):", round(max_temp, 2))

# import numpy as np

# # List of student names
# students = np.array(["Alice", "Bob", "Charlie", "Diana", "Ethan"])

# # Random attendance data: 1 = Present, 0 = Absent
# # Rows = students, Columns = days
# attendance = np.random.randint(0, 2, size=(len(students), 7))

# print("Attendance Matrix (1=Present, 0=Absent):")
# print(attendance)

# # Total days present per student
# total_present = np.sum(attendance, axis=1)

# print("\nTotal Days Present:")
# for i in range(len(students)):
#     print(f"{students[i]}: {total_present[i]} days")

# # Total presence on each day
# daily_attendance = np.sum(attendance, axis=0)
# print("\nDaily Attendance (number of students present each day):")
# print(daily_attendance)
 
import numpy as np 

marks = [60,70,59,84,65,78,95,89]

marks_array = np.array(marks)

Total_marks = np.sum(marks_array)
average_marks = np.average(marks_array)
Minimum_marks = np.min(marks_array)
Maximun_marks = np.max(marks_array)
Sorted_marks = np.sort(marks_array)
Squared_maks = np.square(marks_array)

print("Total marks is ",Total_marks)
print("Average marks is ",average_marks)
print("Minimun marks is ",Minimum_marks)
print("Maximum marks is ",Maximun_marks)
print("Sorted marks is ",Sorted_marks)
print("Squared marks is ",Squared_maks)