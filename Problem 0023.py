# Problem 23
# Find the sum of all positive integers which cannot be written as the sum of two abundant numbers.

import math

int_list = [*range(1, 30000)]


# Takes in a positive integer and determines if it is a perfect number.
def abundant_check(x):
    if x == 1:
        return False
    factor_sum = 1
    i = 2
    if math.sqrt(x) == int(math.sqrt(x)):
        factor_sum += math.sqrt(x)
    while i < math.sqrt(x):
        if x % i == 0:
            factor_sum += i
            factor_sum += (x / i)
        i += 1
    return factor_sum > x

abundant_list = []
for x in int_list:
    if abundant_check(x):
        abundant_list.append(x)

# Create a list of all abundant sums with duplicates.
abundant_sums = []
i = 0
while i < len(abundant_list) - 1:
    j = i
    while abundant_list[i] + abundant_list[j] <= len(int_list) and j < len(abundant_list):
        abundant_sums.append(abundant_list[i] + abundant_list[j])
        j += 1
    i += 1

# Remove duplicates
abundant_sums_set = [*set(abundant_sums)]

# Remove abundant sums from integer list
#i = 0
#while i < len(abundant_sums_set):
#    int_list[abundant_sums_set[i]-1] = 0
#    i += 1

for x in abundant_sums_set:
    int_list.remove(x)


non_abundant_sum = 0
for x in int_list:
    non_abundant_sum += x

# print(len(abundant_sums))
# print(len(abundant_sums_set))
print(int_list)
print(non_abundant_sum)