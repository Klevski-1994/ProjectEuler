# Problem 16
# Find the sum of the digits of 2^{1000}


def power_two_n_digit_sum(n):
    digits = [1]
    i = 1
    while i <= n:
        j = len(digits) - 1
        if digits[j] >= 5:
            digits[j] = digits[j]*2 - 10
            digits.append(1)
        else: 
            digits[j]*=2
        j -= 1
        while j >= 0:
            if digits[j] >= 5:
                digits[j] = digits[j]*2 - 10
                digits[j+1] += 1
            else:
                digits[j] *= 2
            j -= 1
        i += 1
    digit_sum = 0
    for digit in digits:
        digit_sum += digit
    return digit_sum

print(power_two_n_digit_sum(1000))