# Problem 21
# Find the sum of all amicable numbers under 10000.

import math 


# Takes in an integer and finds the sum of all of its factors.
def factor_sum(x):
    if x == 1:
        return 1
    factor_sum = 1
    i = 2
    if math.sqrt(x) == int(math.sqrt(x)):
        factor_sum += math.sqrt(x)
    while i < math.sqrt(x):
        if x % i == 0:
            factor_sum += i
            factor_sum += (x / i)
        i += 1
    return factor_sum

amicable_sum = 0
i = 2
while i < 10000:
    a = factor_sum(i)
    if a == i:
        i += 1
    else:
        b = factor_sum(factor_sum(i))
        if b == i and b <10000 and a < 10000:
            amicable_sum += i
        i += 1


print(amicable_sum)