# Problem 13
# Find the first ten digits of a sum of 100 different 50 digit numbers 

summands_file = open("D:\Python\ProjectEuler Solutions\ProjectEuler\Problem 0013 summands.txt", 'r')


summands_list = []

for line in summands_file:
    line = line.strip()
    summands_list.append(line)

#Specifically requires 50 digit numbers as input.
def line_summer(list):
    i=0
    carryover = 0
    while i<5:
        tempsum = carryover
        j = 0
        while j<100:
            k = 0
            summand_piece = ""
            while k < 10:
                summand_piece += (list[j][50-10*i-(10-k)])
                k += 1
            tempsum += int(summand_piece)
            j += 1

        if i<4:
            carryover = tempsum//pow(10,10)
        else:
            return str(tempsum)
        i += 1


result = line_summer(summands_list)
ten_digits = ""
i = 0
while i <10:
    ten_digits += (result[i])
    i += 1

print(ten_digits)