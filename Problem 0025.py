# Problem 25
# Find index of the first Fibonacci term to contain 1000 digits. 


# Takes string inputs of x and y to return a sum as a string.
def string_sum(x,y):
    sum = ""
    carry = 0
    i = 1
    while i <= len(x) and i <= len(y):
        sum_digit = int(x[-i]) + int(y[-i]) + carry
        if sum_digit >= 10:
            carry = 1
            sum = str(sum_digit - 10) + sum
        else:
            carry = 0
            sum = str(sum_digit) + sum
        i += 1

    while i <= len(x):
        sum_digit = int(x[-i]) + carry
        if sum_digit >= 10:
            carry = 1
            sum = str(sum_digit - 10) + sum
        else:
            carry = 0
            sum = str(sum_digit) + sum
        i += 1

    while i <= len(y):
        sum_digit = int(y[-i]) + carry
        if sum_digit >= 10:
            carry = 1
            sum = str(sum_digit - 10) + sum
        else:
            carry = 0
            sum = str(sum_digit) + sum
        i += 1

    if carry == 1:
        sum = "1" + sum

    return sum


i=2
fibonacci_n_minus_one = "1"
fibonacci_n = "1"
while len(fibonacci_n) < 1000:
    i += 1
    fibonacci_storage = fibonacci_n
    fibonacci_n = string_sum(str(fibonacci_n), str(fibonacci_n_minus_one))
    fibonacci_n_minus_one = fibonacci_storage


print(i)