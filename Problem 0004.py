# Problem 4
# Calculates the largest palindrome that can be made by multiplying two whole numbers below (not including) the target value.


def largest_palindrome_multiple(target_num):
    factors = [*range(1,target_num)]
    factors.reverse()
    largest_palindrome = 0
    for i in factors:
        temp_range = [*range(i,target_num)]
        temp_range.reverse()
        for j in temp_range:
            candidate = i*j
            candidate = str(candidate)
            reverse_candidate = candidate[::-1]
            if candidate == reverse_candidate and int(candidate) > largest_palindrome:
                largest_palindrome = int(candidate)
    return largest_palindrome

print(largest_palindrome_multiple(1000))