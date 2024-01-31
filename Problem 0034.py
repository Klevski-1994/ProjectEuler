# Problem 34
# Find the sum of all numbers which are equal to the sum of the factorials of its digits.

import math

factorial_sum = 0
i = 3
while i <= 2540160:
    j = 0
    temp_sum = 0
    while j < len(str(i)):
        temp_sum += math.factorial(int(str(i)[j]))
        j += 1
    if temp_sum == i:
        print(i)
        factorial_sum += i
    i += 1
    
print(factorial_sum)