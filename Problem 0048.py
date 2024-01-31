# Problem 48
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000

#Not the most proper answer (user needs to count digits), this one didn't motivate me very much.

i = 1
sum = 0
while i < 1000:
    sum += i ** i
    i += 1

print(sum)