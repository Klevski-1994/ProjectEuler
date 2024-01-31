# Problem 20
# Find the sum of the digits in the number 100!


# Input an integer and return a list of its digits. Non-critical function, used here for testing.

def cut_integer(x):
    x_string = str(x)
    x_list = []
    for char in x_string:
        x_list.append(int(char))
    return x_list


# Requires an input of an integer x_list broken into a list (e.g. 420 --> [4,2,0]) and multiplies it by a standalone value y. Returns list.

def multiply_list(x_list, y):
    i = 0
    product = []
    while i < len(x_list):
        digit_product = x_list[-i-1]*y
        digit_product_string = str(digit_product)
        j = 1
        while j <= len(digit_product_string):
            if len(product) < i + j:
                product.insert(0,int(digit_product_string[-j]))
            else:
                digit_value = product[-j-i] + int(digit_product_string[-j])
                if digit_value >= 10:
                    helper = 1
                    resolution = 0
                    product[-j-i] = digit_value - 10
                    while len(product) >= i + j + helper:
                        if product[-j-i-helper] == 9:
                            product[-j-i-helper] = 0
                            helper += 1
                        else: 
                            product[-j-i-helper] += 1
                            resolution = 1
                            break
                    if resolution == 0:
                        product.insert(0,1)
                else:
                    product[-j-i] = digit_value
            j += 1


        i += 1
    


    return product


def factorial_digit_sum(n):
    factorial = [1]
    i = 1
    while i <= n:
        factorial = multiply_list(factorial, i)
        i += 1
    sum = 0
    for digit in factorial:
        sum += digit
    return sum



print(factorial_digit_sum(100))

