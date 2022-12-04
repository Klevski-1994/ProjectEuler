# Problem 6
# Calculate the difference between the square of the sum of the first twenty natural numbers and the sum of the first twenty perfect squares


#Calculates the sum of the first x perfect squares
def sum_of_squares(x):
    sum = 0
    for i in range(1,x+1):
        sum += pow(i,2)
    return sum


#Calculates the sqare of the sum of the first x natural numbers
def square_of_sum(x):
    sum = 0
    for i in range(1,x+1):
        sum += i
    return pow(sum,2)


print(square_of_sum(100)-sum_of_squares(100))



