#Problem 7
#Find the n-th prime number
#NOTE: INEFFICIENT ALGORITHM; REDESIGN BEFORE REUSING


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

#Returns n-th prime number
def nth_prime_number(n): 
    i=2
    prime_list = []
    q = 0
    while q < n:
        if len(prime_factorization(i)) == 1:
            q+=1
        if q == n:
            return i
        elif i == 2:
            i+=1
        else: 
            i+=2


print(nth_prime_number(10001))