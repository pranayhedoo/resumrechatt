import random
 # Possible states
states = ["Sunny", "Rainy"]
 # Transition probabilities
transition = {
 "Sunny": {"Sunny": 0.4, "Rainy": 0.6},
 "Rainy": {"Sunny": 0.5, "Rainy": 0.4}
 }
 # Start state
current_state = "Sunny"
print("Today:", current_state)
# Simulate next 5 days
for i in range(5):
 next_state = random.choices(
 population=["Sunny", "Rainy"],
 weights=[transition[current_state]["Sunny"], transition[current_state]["Rainy"]]
 )[0]
 print("Day", i+1, ":", next_state)
 current_state = next_state