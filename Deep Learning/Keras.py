from keras.models import Sequential
from keras.layers import Dense
import numpy as np
# Dummy data: inputs and targets
X = np.array([[0], [1], [2], [3], [4]], dtype=float)
y = np.array([[0], [1], [4], [9], [16]], dtype=float)  # Squared values
model = Sequential([
    Dense(units=10, input_shape=[1], activation='relu'),
    Dense(units=1)  # Output layer
])
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X, y, epochs=100, verbose=1)
print(model.predict([[5.0]]))  # Predicts value for input 5