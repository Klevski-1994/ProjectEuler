# Problem 5
# Calculates the largest number that is evenly divisible by all integers from 1 to the target number (in this case 20)


#Returns a list of the prime factors of a number (with duplicates)
def prime_factorization(x):
    if x<=1 or x/1 != x//1:
        print("Error: attempted to find the prime factorization of an unsuitable number")
        return []
    else:
        prime_factorization_list = []
        i=2
        while i <= x:
            if x % i == 0:
                prime_factorization_list.append(i)
                x /= i
            else:
                if i == 2:
                    i+=1
                else:
                    i+=2
    return prime_factorization_list


#Returns a list of prime numbers at or below the input value
def upper_bound_prime_list(x): 
    i=2
    prime_list = []
    while i <= x:
        if len(prime_factorization(i)) == 1:
            prime_list.append(i)
        i+=1
    return prime_list


#Returns the least common multiple of all whole numbers at or below the input value
def least_common_multiple_upper_bound(x):
    i = 2
    lesser_primes = upper_bound_prime_list(x)
    power_list = []
    for p in lesser_primes:
        power_list.append(1)
    while i<=x:
        prime_factors_list = prime_factorization(i)
        q = 0
        while q < len(lesser_primes):
            prime_count = prime_factors_list.count(lesser_primes[q])
            if prime_count >= power_list[q]:
                power_list[q]= prime_count
            q+=1
        i+=1
    least_common_multiple = 1
    for i in range(0,len(power_list)):
        least_common_multiple *= pow(lesser_primes[i],power_list[i])
    return least_common_multiple


print(least_common_multiple_upper_bound(20))