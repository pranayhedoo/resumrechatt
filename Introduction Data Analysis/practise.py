import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed()  # for reproducibility

data = {
    'Id': range(1, 8),
    'SSC': np.random.randint(60, 100, 7),
    'HSC': np.random.randint(55, 95, 7),
    'Degree': np.random.randint(65, 100, 7)
}

df = pd.DataFrame(data)
print(df)

print("First Two rows:\n", df.head(2))
print("\nSummary statistics:\n", df.describe())
