import matplotlib.pyplot as plt

def count_combinations(coins_list, amount, max_coin):
    total = 0
    if amount == 0:
        total += 1
    for coin in coins_list:
        if coin <= amount and coin <= max_coin:
            total += count_combinations(coins_list, amount - coin, coin)
    return total

if __name__ == "__main__":
    print("2) b. " + str(count_combinations([1,5,10,25], 213, 1000)))
    print("   c. " + str(count_combinations([1,5,10], 213, 1000)))
    x = []
    y = []
    for val in range(500):
        x.append(val)
        y.append(count_combinations([1,5,10,25], val, 1000))
    plt.xlabel("Target amount")
    plt.ylabel("Number of combinations")
    plt.plot(x, y)
    plt.savefig("fig2d")
    