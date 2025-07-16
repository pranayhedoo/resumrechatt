# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense

# print("TensorFlow LSTM imports successful!")

# import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense

# # Input data: sequences like [1,2,3] -> [4]
# X = np.array([
#     [[1], [2], [3]],
#     [[2], [3], [4]],
#     [[3], [4], [5]],
#     [[4], [5], [6]],
# ])
# y = np.array([4, 5, 6, 7])

# # Build the model
# model = Sequential()
# model.add(LSTM(50, input_shape=(3, 1)))  # 3 time steps, 1 feature
# model.add(Dense(1))  # Output layer

# model.compile(optimizer='adam', loss='mse')

# # Train the model
# model.fit(X, y, epochs=200, verbose=0)

# # Test the model: Predict next number after [5,6,7]
# test_input = np.array([[[5], [6], [7]]])
# predicted = model.predict(test_input)
# print("Predicted value:", predicted)


# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, LSTM, TimeDistributed, Dense
# from tensorflow.keras.utils import to_categorical
# import numpy as np
#  # Step 1: Word and Tag mapping
# word2idx = {'PAD': 0, 'John': 1, 'lives': 2, 'in': 3, 'Paris': 4}
# tag2idx = {'PAD': 0, 'O': 1, 'PERSON': 2, 'LOCATION': 3}
#  # Step 2: Prepare input and output
# X = [[1, 2, 3, 4]]         
# # "John lives in Paris"
# y = [[2, 1, 1, 3]]        
#  # [PERSON, O, O, LOCATION]
#  # Step 3: One-hot encode the output tags
# y = to_categorical(y, num_classes=len(tag2idx))
#  # Step 4: Build a simple LSTM model
# model = Sequential()
# model.add(Embedding(input_dim=len(word2idx), output_dim=8, input_length=4))
# model.add(LSTM(16, return_sequences=True))
# model.add(TimeDistributed(Dense(len(tag2idx), activation='softmax')))
#  # Step 5: Train
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.fit(np.array(X), y, epochs=100, verbose=0)
#  # Step 6: Predict
# prediction = model.predict(np.array(X))
# pred_tags = np.argmax(prediction, axis=-1)
# print("Predicted Tags:", pred_tags[0])

# import tensorflow as tf
# print(tf.__version__)

# import torch
# import torch.nn as nn
# import numpy as np

# # Sample data
# X = np.array([[1, 2, 3], [2, 3, 4]], dtype=np.float32)
# y = np.array([4, 5], dtype=np.float32)

# X = torch.tensor(X.reshape(2, 3, 1))
# y = torch.tensor(y.reshape(2, 1))

# # Define LSTM Model
# class SimpleLSTM(nn.Module):
#     def __init__(self):
#         super(SimpleLSTM, self).__init__()
#         self.lstm = nn.LSTM(input_size=1, hidden_size=10, batch_first=True)
#         self.fc = nn.Linear(10, 1)

#     def forward(self, x):
#         out, _ = self.lstm(x)
#         out = self.fc(out[:, -1, :])
#         return out

# model = SimpleLSTM()
# criterion = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# # Train loop
# for epoch in range(100):
#     output = model(X)
#     loss = criterion(output, y)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# import torch
# import torch.nn as nn

# # Simple data: 2 sequences, 3 steps each
# X = torch.tensor([[[1.0], [2.0], [3.0]],
#                   [[2.0], [3.0], [4.0]]])
# y = torch.tensor([[4.0], [5.0]])

# # Define a basic LSTM model
# model = nn.Sequential(
#     nn.LSTM(input_size=1, hidden_size=10, batch_first=True),
#     nn.Linear(10, 1)
# )

# # Loss and optimizer
# loss_fn = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# # Training loop
# for _ in range(100):
#     pred, _ = model[0](X)              # LSTM output
#     out = model[1](pred[:, -1, :])     # Use last time step
#     loss = loss_fn(out, y)

#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

# # Test prediction
# test = torch.tensor([[[3.0], [4.0], [5.0]]])
# pred_test, _ = model[0](test)
# result = model[1](pred_test[:, -1, :])
# print("Predicted value:", result.item())


# import torch
# import torch.nn as nn
# import numpy as np

# # Sample data
# X = np.array([[1, 2, 3], [2, 3, 4]], dtype=np.float32)
# y = np.array([4, 5], dtype=np.float32)

# X = torch.tensor(X.reshape(2, 3, 1))
# y = torch.tensor(y.reshape(2, 1))

# # Define LSTM Model
# class SimpleLSTM(nn.Module):
#     def __init__(self):
#         super(SimpleLSTM, self).__init__()
#         self.lstm = nn.LSTM(input_size=1, hidden_size=10, batch_first=True)
#         self.fc = nn.Linear(10, 1)

#     def forward(self, x):
#         out, _ = self.lstm(x)
#         out = self.fc(out[:, -1, :])
#         return out

# model = SimpleLSTM()
# criterion = nn.MSELoss()
# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# # Train loop with loss printing
# for epoch in range(100):
#     output = model(X)
#     loss = criterion(output, y)
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     # Print loss every 10 epochs
#     if (epoch + 1) % 10 == 0:
#         print(f'Epoch {epoch + 1}, Loss: {loss.item():.4f}')

# # Final prediction example
# with torch.no_grad():
#     test_input = torch.tensor([[[3.0], [4.0], [5.0]]])
#     prediction = model(test_input)
#     print("Predicted value:", prediction.item())

import torch
import torch.nn as nn

# Sample sequence data
X = torch.tensor([[[1.0], [2.0], [3.0]]])  # Shape: (batch=1, steps=3, features=1)
y = torch.tensor([[4.0]])  # Expected next value

# Simple LSTM model
class SimpleLSTM(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=10, batch_first=True)
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])
 
model = SimpleLSTM()
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# Training loop
for epoch in range(100):
    output = model(X)
    loss = criterion(output, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 20 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

# Prediction
with torch.no_grad():
    pred = model(X)
    print("Predicted next value:", pred.item())
