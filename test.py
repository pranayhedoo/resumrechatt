# # Using a context manager to open and read a file
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)
# # File is automatically closed here

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
 # Simple NN for binary classification
model = Sequential([
 Dense(10, activation='relu', input_shape=(5,)),
 Dense(1, activation='sigmoid')
 ])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()
import numpy as np
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, 100)
 # Fit the model
model.fit(X, y, epochs=10, batch_size=8)