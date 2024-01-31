# Problem 14
# The goal of this program is to find the longest Collatz Conjecture chain for starting points under one million. 



checkables = [*range(1000000)]

def collatz_chain_length(number):
    print(number)
    count = 1
    global checkables
    while number != 1:
        count += 1
        if(number % 2 == 0):
            number //= 2
        else:
            number *= 3
            number += 1
        if number < 1000000:
            checkables[number] = 1
    return count


def collatz_checker():
    global checkables
    current_max_chain = 1
    current_max_start = 1
    i = 1
    while i<1000000:
        if checkables[i] > 1:
            chain_check = collatz_chain_length(checkables[i])
            if chain_check  > current_max_chain:
                current_max_chain = chain_check
                current_max_start = i
        i += 1
    return current_max_start


print(collatz_checker())