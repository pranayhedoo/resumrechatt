# import pandas as pd 

# # Sample dataset
# data = {
#  'Student': ['Amit', 'Neha', 'Raj', 'Simran', 'Neha', 'Ravi'],
#  'Math_Score': [85, 90, 78, 92, 90, 85]
#  }
# df = pd.DataFrame(data)
#  # EDA steps:
# print("\n2. Summary statistics:\n", df.describe())
# print("\n3. Missing values:\n", df.isnull().sum())
# print("\n4. Duplicate rows:\n", df.duplicated().sum())

import pandas as pd

# Sample dataset
data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet', 'Mobile', 'Smartphone', 'Laptop'],
    'Sales': [1200, 1500, 800, 600, 1500, None]
}
df = pd.DataFrame(data)

# EDA steps:
print("\n2. Summary statistics:\n", df.describe())
print("\n3. Missing values:\n", df.isnull().sum())
print("\n4. Duplicate rows:\n", df.duplicated().sum())
