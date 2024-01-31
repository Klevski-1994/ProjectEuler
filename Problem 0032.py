# Problem 32
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.


def pandigital_product_finder():
    pan_list = []
    multiplicand = 1
    while multiplicand < 100:
        multiplier = 9999 // multiplicand
        while multiplier >100:
            temp_string = str(multiplicand * multiplier) + str(multiplicand) + str(multiplier)
            if len(temp_string) == 9:
                if str(1) in temp_string:
                    if str(2) in temp_string:
                        if str(3) in temp_string:
                            if str(4) in temp_string:
                                if str(5) in temp_string:
                                    if str(6) in temp_string:
                                        if str(7) in temp_string:
                                            if str(8) in temp_string:
                                                if str(9) in temp_string:
                                                    pan_list.append((multiplicand, multiplier, multiplicand*multiplier))
                                                            
            multiplier -= 1
        multiplicand += 1

    return set(pan_list)


pan_product_list = (pandigital_product_finder())
pan_product_set = []
pan_product_sum = 0
for tuple in pan_product_list:
    pan_product_set.append(tuple[2])
pan_product_set = set(pan_product_set)
for product in pan_product_set:
    pan_product_sum += product

print(pan_product_list)
print(pan_product_set)
print(pan_product_sum)