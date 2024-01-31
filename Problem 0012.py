# Problem 12
# Finds first triangle number whose divisor count exceeds 500. 

import math

current_triangle = 1
increment = 2

while current_triangle <=999:
    current_triangle += increment
    increment += 1


# Creates a list of all the prime factorization of the input number (with duplicates).
def prime_factorization(x):
    if x<=1 or x/1 != x//1:
        print("Error: attempted to find the prime factorization of an unsuitable number")
        return []
    else:
        prime_factorization_list = []
        i=1
        while x >= 2 and x % 2 == 0:
            prime_factorization_list.append(2)
            x /= 2
        while x >= 3 and x % 3 == 0:
            prime_factorization_list.append(3)
            x /= 3
        i = 6
        while i - 1 <= x:
            p = i-1
            while x % p == 0:
                prime_factorization_list.append(p)
                x/=p
            p += 2
            while x % p == 0:
                prime_factorization_list.append(p)
                x/=p
            i += 6

    return prime_factorization_list



# Requires prime_factorization(x) helper function. Evaluates the number of divisors a number has by evaluating its prime factorization.
def divisor_count(n):
    if n == 1:
        return 1
    prime_factors = prime_factorization(n)
    prime_count = len(prime_factors)
    divisors = 1
    multi = 2
    i = 1
    while i < prime_count:
        if prime_factors[i] == prime_factors[i-1]:
            multi += 1
            if i == prime_count - 1:
                divisors *= multi
                return divisors
            i += 1

        else:
            divisors *= multi
            multi = 2
            i += 1
    divisors *= multi
    return divisors



while True:
    if divisor_count(current_triangle) > 500:
        print(current_triangle)
        break
    current_triangle += increment
    increment += 1
