# Problem 28
# Sum the diagonals on a number spiral as constructed at https://projecteuler.net/problem=28. 

# This code will be pretty lazy because there is a "simple" pattern that will add together all these diagonals. 


# Input is the side dimensions of the square spiral. Only works for odd square dimensions. 

def spiral_sum(n):
    if n / 1 != n//1 or n < 0 or n // 2 == n/2:
        return "Please input an odd positive integer."
    if n == 0:
        return 0
    if n == 1:
        return 1
    sum_total = 1
    k = 1
    j = 1
    while j < n:
        j += 2
        i = 0
        while i < 4:
            k += (j-1)
            sum_total += k
            i += 1
        
    return sum_total

print(spiral_sum(1001))