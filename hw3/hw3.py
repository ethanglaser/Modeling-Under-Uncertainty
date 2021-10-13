import numpy as np
import matplotlib.pyplot as plt

def markov(num, matrix, start, fig=''):
    out = []
    current = start
    for _ in range(num):
        out.append(current)
        current = np.random.choice([1,2,3], p=matrix[current-1])
    if fig:
        plt.figure()
        plt.xlabel('n')
        plt.ylabel('state')
        plt.scatter(range(len(out)), out)
        plt.savefig(fig)
    else:
        return out

matrix = [[.4, .38, .22], [.12, .7, .18], [.2, .5, .3]]
markov(100, matrix, 1, fig='3a')
out = markov(1000, matrix, 1)
print("3b.")
print("Average over 1000 simultations: " + str(sum(out) / len(out)))
print("Sum using Beta=0.9: " + str(sum([0.9 ** index * val ** 2 for index, val in enumerate(out)])))

one, two = [], []
for _ in range(1000):
    out = markov(1000, matrix, 1)
    one.append(sum(out) / len(out))
    two.append(sum([0.9 ** index * val ** 2 for index, val in enumerate(out)]))
print("3c.")
print("Average of first over 1000 reps of 1000 simulations: " + str(sum(one) / len(one)))
print("Average of second over 1000 reps of 1000 simulations: " + str(sum(two) / len(two)))
