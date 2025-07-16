# import matplotlib.pyplot as plt

# # Sample data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Create a line plot
# plt.plot(x, y)

# # Add labels and title
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Simple Line Graph")

# # Show the plot
# plt.show()


      #    bar chart

# import matplotlib.pyplot as plt

# # Sample data
# students = ['Alice', 'Bob', 'Charlie', 'Diana']
# marks = [85, 90, 78, 92]

# # Create a bar chart
# plt.bar(students, marks, color='skyblue')

# # Add labels and title
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Marks of Students")

# # Show the plot
# plt.show()

     #    Scattered chart

# import matplotlib.pyplot as plt

# # Sample data
# height = [150, 160, 170, 180, 190]
# weight = [50, 60, 65, 80, 85]

# # Create a scatter plot
# plt.scatter(height, weight, color='green')

# # Add labels and title
# plt.xlabel("Height (cm)")
# plt.ylabel("Weight (kg)")
# plt.title("Height vs Weight")

# # Show the plot
# plt.show()

     #    Histogram chart

import matplotlib.pyplot as plt

# New sample data: heights of students (in cm)
heights = [150, 152, 158, 160, 165, 168, 170, 172, 175, 178, 180, 182, 185, 188, 190, 195]

# Create a histogram
plt.hist(heights, bins=6, color='skyblue', edgecolor='black')

# Add labels and title
plt.xlabel("Height Range (cm)")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Heights")

# Show the plot
plt.show()


    #    Pie chart

# import matplotlib.pyplot as plt

# # Sample data
# activities = ['Study', 'Sleep', 'Exercise', 'Leisure']
# hours = [6, 8, 2, 8]

# # Create a pie chart
# plt.pie(hours, labels=activities, autopct='%1.1f%%', startangle=90)

# # Add title
# plt.title("Daily Time Spent on Activities")

# # Show the plot
# plt.show()
