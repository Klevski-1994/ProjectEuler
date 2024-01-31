# Problem 31
# Using 1p, 2p, 5p, 10p, 20p, 50p, 1 pound, and 2 pound coins, how many ways can you make two pounds?

# Another way to frame this is "How many sets containing only the numbers 1, 2, 5, 10, 20, 50, 100, and 200 would sum to 200?"


sol_count = 0


coin_set = [1, 2, 5, 10, 20, 50, 100, 200]
def coin_increment(coin, current_val):
    while current_val <= 200:
        if current_val < 200 and coin < (len(coin_set) - 1):
            coin_increment(coin + 1, current_val)
        if current_val == 200:
            global sol_count
            sol_count += 1
        current_val += coin_set[coin]

    return

coin_increment(0,0)

print(sol_count)