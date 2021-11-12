import numpy as np
import matplotlib.pyplot as plt

matrix = [[0, .6, .4], [.3, 0, .7], [.85, .15, 0]]
rate = [0.1, 0.2, 0.3]

def sim():
    times = []
    states = []
    reward = 0
    current = 1
    while len(times) == 0 or times[-1] < 1000:
        current_t = np.random.exponential(1 / rate[current - 1])
        times.append(current_t)
        if len(times) > 1:
            times[-1] += times[-2]
        states.append(current)
        reward += current ** 2 * current_t
        current = np.random.choice([1,2,3], p=matrix[current-1])
    reward /= times[-1]
    times[-1] = 1000
    return times, states, reward

times, states, reward = sim()
plt.figure()
plt.xlabel("Time")
plt.ylabel("State")
plt.step(times, states)
plt.savefig('4a')

tot = 0
for _ in range(100):
    tot += sim()[2]
print("Actual reward (average from 100 simulations):", tot/100)
print("Predicted reward: 3.12")
