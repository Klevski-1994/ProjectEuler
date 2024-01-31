# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20 x 20 grid?

# For the 2 x 2 grid, note that path must travel down exactly twice and right exactly twice. We then ask how many ways we can order these two ups and two downs. 
# If we number the moves (1, 2, 3, 4), we could simply say, "Pick two numbers to be the right move. How many combinations of numbers can you pick?"
# This turns the 2 x 2 problem into 4 choose 2. This framing generalizes to higher grid sizes (including non-square grids) and renders the 20 x 20 problem as simply calculating 40 choose 20.

# Generates a nested list representing Pascal's Triangle up to row n (zero-initialized)
def pascal_generator_function(n):
    pascal_list = [[1]]
    i = 1
    while i <= n:
        pascal_row = [1]
        j=1
        while j < i:
            pascal_row_add = pascal_list[i-1][j-1] + pascal_list[i-1][j]
            pascal_row.append(pascal_row_add)
            j += 1
        pascal_row.append(1)
        pascal_list.append(pascal_row)
        i += 1
    return pascal_list


def n_choose_k(n,k):
    pascal_triangle = pascal_generator_function(n)
    return pascal_triangle[n][k]


print (n_choose_k(40,20))