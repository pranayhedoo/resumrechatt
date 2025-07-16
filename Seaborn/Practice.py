# import seaborn as sns
# import matplotlib.pyplot as plt

# # Sample data
# data = sns.load_dataset("iris")  # Built-in dataset in Seaborn

# # Create a scatter plot
# sns.scatterplot(x='sepal_length', y='sepal_width', data=data)

# # Add title
# plt.title("Sepal Length vs Width")

# # Show the plot
# plt.show()

    #    Barplot chart

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Sample data
# students = ['Alice', 'Bob', 'Charlie', 'Diana']
# marks = [85, 90, 78, 92]

# # Create a dictionary to convert into DataFrame
# import pandas as pd
# data = pd.DataFrame({'Student': students, 'Marks': marks})

# # Create a bar plot
# sns.barplot(x='Student', y='Marks', data=data, palette='Blues')

# # Add a title
# plt.title("Student Marks")

# # Show the plot
# plt.show()

    #   Boxplot 

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load example dataset
# data = sns.load_dataset("tips")  # Contains restaurant bill and tip data

# # Create a box plot
# sns.boxplot(x='day', y='total_bill', data=data, palette='pastel')

# # Add title
# plt.title("Total Bill Distribution per Day")

# # Show the plot
# plt.show()

    #    Heatmap

# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# # Sample 2D data (e.g., student marks in subjects)
# data = np.array([
#     [85, 90, 88],
#     [78, 81, 79],
#     [92, 89, 94],
#     [70, 75, 73]
# ])

# # Subject and student labels
# students = ['Alice', 'Bob', 'Charlie', 'Diana']
# subjects = ['Math', 'Science', 'English']

# # Create a heatmap
# sns.heatmap(data, annot=True, xticklabels=subjects, yticklabels=students, cmap='YlGnBu')

# # Add title
# plt.title("Student Marks Heatmap")

# # Show the plot
# plt.show()

    #    histplot()

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load a built-in dataset
# data = sns.load_dataset("tips")

# # Create a histogram of total bill amounts
# sns.histplot(data['total_bill'], bins=10, color='skyblue', kde=True)

# # Add title and labels
# plt.title("Distribution of Total Bills")
# plt.xlabel("Total Bill")
# plt.ylabel("Frequency")

# # Show the plot
# plt.show()

    #   line chart

import seaborn as sns
import matplotlib.pyplot as plt

# New Data: Monthly Rainfall (in mm)
months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = [160, 145, 120, 95, 60, 40]

# Create line chart
sns.lineplot(x=months, y=rainfall, marker='s', color='green', linewidth=2)

# Add title and labels
plt.title('Average Monthly Rainfall (Jul - Dec)')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')

# Show the plot
plt.show()
