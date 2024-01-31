# Problem 33
# Find the product of all 2-digit fractions which share a digit between numerator and denominator and retain the same value when those like digits are cancelled out. 


# I just wrote code to find these special fractions and multiplied after.
i = 10
while i < 99:
    j = i + 1
    while j <= 99:
        if i // 10 != i/10 and j//10 != j/10:
            if str(i)[0] == str(j)[0]:
                if i / j == int(str(i)[1]) / int(str(j)[1]):
                    print((i,j))
            if str(i)[1] == str(j)[0]:
                if i / j == int(str(i)[0]) / int(str(j)[1]):
                    print((i,j))
            if str(i)[0] == str(j)[1]:
                if i / j == int(str(i)[1]) / int(str(j)[0]):
                    print((i,j))
            if str(i)[1] == str(j)[1]:
                if i / j == int(str(i)[0]) / int(str(j)[0]):
                    print((i,j))

        j += 1
    i += 1


print(1/4 * 1/5 * 2/5 * 1/2)