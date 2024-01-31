# Problem 24
# Find the millionth lexicographic permutation of the digits, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

import math

# Finds the nth permutation of the ten single digit numbers based on lexicographic order.
def nth_lexicographic_permutation(n):
    n -= 1
    if n >= math.factorial(10):
        print("Error: there are not that many permutations.")
        return
    term_list = [*range(0, 10)]
    permutation = []
    i = len(term_list) - 1
    while i >= 0:
        next_digit = term_list[n//math.factorial(i)]
        del term_list[n//math.factorial(i)]
        permutation.append(next_digit)
        n = n % math.factorial(i)
        i -= 1

    return permutation


print(nth_lexicographic_permutation(1000000))