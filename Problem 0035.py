# Problem 35
# Find all prime numbers below one million which are still primes for all rotations of the prime's digits.

import math

# Returns a list of all prime numbers below the target value. Requires helper function is_prime.
def prime_list(x):
    prime_list = []
    if x >= 2:
        prime_list.append(2)
    if x >= 3:
        prime_list.append(3)
    i = 6
    while i - 1 < x:
        p = i-1
        if is_prime(p, prime_list):
            prime_list.append(p)
        p += 2
        if p < x:
            if is_prime(p, prime_list):
                prime_list.append(p)
        i += 6
    return prime_list

# Returns whether a number is prime. Requires an ascending list of all prime numbers below the square root of the value being checked. 
def is_prime(x, list):
    for i in list:
        if x % i == 0:
            return False
        elif i > math.sqrt(x):
            return True
    return True

# Moves the last character of a string to the front.
def string_cycle(string):
    if len(string) == 1:
        return string
    else:
        string_list = []
        for i in string:
            string_list.append(i)
        string_list.insert(0, string_list.pop(-1))
        newstring = ""
        for i in string_list:
            newstring += i
        return newstring

print(string_cycle("Hello"))

prime_list = prime_list(1000000)
circular_prime_list = []

for i in prime_list:
    circular_prime = True
    j = 1
    i_string = str(i)
    while j < len(i_string):
        i_string = string_cycle(i_string)
        if not is_prime(int(i_string), prime_list):
            circular_prime = False
            break
        j += 1
    if circular_prime:
        circular_prime_list.append(i)



print(circular_prime_list)
print(len(circular_prime_list))