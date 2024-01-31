# Problem 22
# Given a list of unsorted names, find the sum of the "name scores" of all items in the list, where a name's score is defined as the product of the name's position and the sum of its constituant letters' alphabetical positions. 

name_file = open("D:\Python\ProjectEuler Solutions\ProjectEuler\Problem 0022 names.txt", 'r')



name_string = str(name_file.readlines())
name_string = name_string.replace('[','')
name_string = name_string.replace(']','')
name_string = name_string.replace("'",'')
name_string = name_string.replace('"','')
name_list = name_string.split(',')
name_list.sort()

scoresum = 0
i = 1
while i <= len(name_list):
    name_sum = 0
    for char in name_list[i-1]:
        name_sum += (ord(char) - 64)
    scoresum += name_sum * i
    i += 1

print(scoresum)