# Problem 18
# Given a finite triangle of numbers similar to Pascal's Triangle (but with arbitrary numerical values), find the path from top to bottom with the maximum sum.

# Real File
pyramid_file = open("D:\Python\ProjectEuler Solutions\ProjectEuler\Problem 0067 pyramid.txt", 'r')

# Test File
#pyramid_file = open("D:\Python\ProjectEuler Solutions\ProjectEuler\Problem 0018 test pyramid.txt", 'r')

pyramid = []    

for line in pyramid_file:
    line = line.strip()
    pyramid.append([int(x) for x in line.split(" ")])


# Takes in a 'pyramid' (in the form of a nested list, where each sub-list is one element longer than the last) of integers and calculates the highest sum path. 
# Function logic changes each value to the highest sum path to reach it, cutting down repeated calculations.
def pyramid_sum_pather(pyramid_list):
    rows = len(pyramid_list)
    i = 1
    while i < rows:
        print(pyramid_list)
        row_width = i+1
        pyramid_list[i][0] += pyramid_list[i-1][0]
        j = 1
        while j < row_width - 1:
            if pyramid_list[i-1][j-1] > pyramid_list[i-1][j]:
                pyramid_list[i][j] += pyramid_list[i-1][j-1]
            else:
                pyramid_list[i][j] += pyramid_list[i-1][j]
            j+= 1
        pyramid_list[i][j] += pyramid_list[i-1][j-1]
        i += 1
    return max(pyramid_list[i-1])

print (pyramid)
print (pyramid_sum_pather(pyramid))