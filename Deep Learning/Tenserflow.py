# import tensorflow as tf

# dataset = tf.data.experimental.make_csv_dataset(
#     'sample.csv',
#     batch_size=32,
#     label_name='target',
#     num_epochs=1
# )

# from keras.models import Sequential
# from keras.layers import SimpleRNN, Dense
#  # Build a simple RNN model
# model = Sequential()
# model.add(SimpleRNN(units=10, input_shape=(5, 1)))  # sequence length = 5, features = 1

# model.add(Dense(1))  # output layer
#  # Compile the model
# model.compile(optimizer='adam', loss='mse')
#  # Summary
# model.summary()

import tensorflow as tf
import numpy as np

# Sample data (x: hours studied, y: test score)
x_train = np.array([1, 2, 3, 4, 5], dtype=float)
y_train = np.array([2, 4, 6, 8, 10], dtype=float)

# Define a simple model with 1 dense layer (1 neuron)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=500, verbose=0)

# Predict a new value
print("Predicted value for x=6:", model.predict([6.0])[0][0])
