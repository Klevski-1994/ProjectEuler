# Problem 30
# Find the sum of all numbers that can be written as the sum of fifth powers of their digits.

# The largest number that could possibly work for six digits would be 6 * 9^5 = 354294, which will be our upper bound.

sum_of_sums = 0
i = 10
while i <= 354294:
    str_i = str(i)
    string_power_sum = 0
    for char in str_i:
        string_power_sum += int(char)**5
    if string_power_sum == i:
        sum_of_sums += i
    i += 1

print(sum_of_sums)