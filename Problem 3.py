#Problem 3
#Calculates the largest prime factor of the input number. 
import math

target_num = input("Enter an integer greater than 1 to get its largest prime factor:")
target_num = int(target_num)

def largest_prime_factor(factor_number):
    i = 2
    while i <= math.sqrt(factor_number):
        if factor_number % i == 0:
            factor_number /= i
        elif i == 2:
            i += 1
        else:
             i += 2
    return factor_number

print(int(largest_prime_factor(target_num)))