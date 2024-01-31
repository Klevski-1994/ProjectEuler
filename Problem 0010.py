# Problem 10
# Calculates the sum of all primes below the target value (in this case, 2,000,000)

#NOTE: can be sped up with an implementation using the sieve of Eratosthenes


import math

# Adds together all prime numbers below the target value. Requires helper function is_prime
def upper_bound_prime_sum(x):
    prime_sum = 0
    prime_list = []
    if x >= 2:
        prime_list.append(2)
        prime_sum += 2
    if x >= 3:
        prime_list.append(3)
        prime_sum += 3
    i = 6
    while i - 1 < x:
        p = i-1
        if is_prime(p, prime_list):
            prime_list.append(p)
            prime_sum += p
        p += 2
        if p < x:
            if is_prime(p, prime_list):
                prime_list.append(p)
                prime_sum += p
        i += 6
    return prime_sum

# Takes in a value and a list. Returns True or False dependent upon whether any of the numbers in the list is a factor of the value.
def has_factor_in_list(x, list):
    for i in list:
        if x % i == 0:
            return True
    return False

# Like the above function, but specifically for the purpose of checking for prime numbers. Computationally faster. Requires an ascending list of all prime numbers below the square root of the value being checked. 
def is_prime(x, list):
    for i in list:
        if x % i == 0:
            return False
        elif i > math.sqrt(x):
            return True
    return True


print(upper_bound_prime_sum(2000000))