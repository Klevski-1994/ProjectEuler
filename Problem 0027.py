# Problem 27
# For |a| < 1000 and |b|<=1000, find the product of a and b which finds the maximum number of primes for consecutive values of n in the function f(n) = n^2 + an + b

import math

def quadratic(x, a, b):
    return (x ** 2 + a*x + b)


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

# Determines whether a given integer is odd or even.
def is_odd(x):
    if x/2 == x//2:
        return False
    elif (x+1)/2 == (x+1)//2:
        return True
    else: return None




# For |a| < a_max and |b|<= b_max, returns the value of a and b which finds the maximum number of primes for consecutive values of n in the function f(n) = n^2 + an + b
def greatest_prime_consecutive_quadratic_finder(a_max, b_max):

    max_consecutive = (0,0,0)
    prime_factors = prime_list(quadratic(79,a_max, b_max))

    # Finds possible values for b, as b must be prime and positive.

    b_list = prime_list(b_max)

    #b_list_neg = []
    #for i in b_list_pos:
    #    b_list_neg = [(-1*i)] + b_list_neg
    #b_list = b_list_neg + b_list_pos

    # Finds possible values for a matched to a given b. For a to be viable for a given b, 1 + a + b must be prime. 
    # Assumes a and b are sufficiently large for more than two consecutive primes. In this case, a must be odd to achieve anything more than a streak of 2 (parity preservation)
    
    a_list = []
    for i in b_list:
        a_iterate = -1*a_max + 1
        if not is_odd(a_iterate):
            a_iterate += 1

        temp_list = []
        while a_iterate < a_max:
            if (a_iterate + i + 1 >= 0):
                if is_prime(a_iterate + i + 1, prime_factors):
                    temp_list.append(a_iterate)
            a_iterate += 2
        
        a_list.append(temp_list)
    
    i = 0

    print(b_list)
    print(a_list)
    while i < len(b_list):
        j = 0
        while j < len(a_list[i]):
            n = 2
            while quadratic(n, a_list[i][j], b_list[i]) > 0:
                if is_prime(quadratic(n, a_list[i][j], b_list[i]), prime_factors):
                    n += 1
                else: break
            if n > max_consecutive[0]:
                max_consecutive = (n, a_list[i][j], b_list[i])
            j+=1
        i+=1

    if max_consecutive == (0,0,0):
        return None 
    else:
        return max_consecutive

print(greatest_prime_consecutive_quadratic_finder(1000,1000))