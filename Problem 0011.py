# Problem 11
# Finds the greatest product of four adjacent numbers in the same cardinal or intermediate direction.

array_file = open("D:\Python\ProjectEuler Solutions\ProjectEuler\Problem 0011 grid.txt", 'r')


array_set = []

for line in array_file:
    line = line.strip()
    array_set.append(line.split(" "))

for item in array_set:
    for sub in item:
        sub = int(sub)

# Function for testing all the four-in-a-row-products. Iterates through each column, then row, then negative slope diagonals, then positive slope diagonals. 
# Takes in a rectangular array as the first term and the number of consecutive terms to multiply as the second term.
def array_product_comb(target_array, n):
    x_max = len(target_array[0])
    y_max = len(target_array)

    row = 0
    col = 0
    candidate = 0


    # Vertical multiplication
    while row <= y_max - n:
        while col < x_max:
            test_candidate = 1
            for i in range(n):
                test_candidate *= int(array_set[row + i][col])
            if test_candidate > candidate:
                candidate = test_candidate
            col += 1
        row += 1
        col = 0
    row = 0
    col = 0


    # Horizontal multiplication
    while row < y_max:
        while col <= x_max - n:
            test_candidate = 1
            for i in range(n):
                test_candidate *= int(array_set[row][col + i])
            if test_candidate > candidate:
                candidate = test_candidate
            col += 1
        row += 1
        col = 0
    row = n-1
    col = 0


    #Positive slope diagonal multiplication
    while row < y_max:
        while col <= x_max - n:
            test_candidate = 1
            for i in range(n):
                test_candidate *= int(array_set[row - i][col + i])
            if test_candidate > candidate:
                candidate = test_candidate
            col += 1
        row += 1
        col = 0
    row = 0
    col = 0
    

    while row <= y_max - n:
        while col <= x_max - n:
            test_candidate = 1
            for i in range(n):
                test_candidate *= int(array_set[row + i][col + i])
            if test_candidate > candidate:
                candidate = test_candidate
            col += 1
        row += 1
        col = 0
        

    return candidate


print(array_product_comb(array_set, 4))