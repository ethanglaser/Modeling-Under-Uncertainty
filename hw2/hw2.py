import numpy as np
from matplotlib import pyplot as plt

def experiment(target):
    total = 0
    tries = 0
    while total < target:
        total += np.random.uniform()
        tries += 1
    return tries

print("2a.")
for target in [1, 2]:
    for experiments in [100, 1000, 10000]:
        print("Estimated E[N" + str(target) + "] from generating " + str(experiments) + " values of N" 
        + str(target) + ": " + str(sum([experiment(target) for i in range(experiments)]) / experiments))



print("5.")
def maximize(p, c, t, num_tests):
    income = p * np.random.poisson(np.log(1 + t), num_tests) - t * c
    return np.average(income)

x, y = [], []
for t in range(11):
    x.append(t)
    y.append(maximize(12, 3, t, 100000))

plt.plot(x, y)
plt.savefig('hw2_5')

print("Optimal number of hours worked is " + str(y.index(max(y))))

