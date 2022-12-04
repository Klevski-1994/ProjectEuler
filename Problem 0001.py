#Problem 1
#For a user defined input, calculates the sum of all multiples of either 3 or 5 below the input number.

upperBound = input("Enter non-inclusive ceiling:")
upperBound = int(upperBound)
sumTotal = int(0)
for i in range(1,int(upperBound)):
    if i/3 == i//3:
        sumTotal += i
    elif i/5 == i//5:
        sumTotal += i

print(sumTotal)