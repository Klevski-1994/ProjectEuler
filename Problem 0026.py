# Problem 26
# Find the unit fraction under 1000 whose decimal has the longest repeating string of digits. 


def recurring_cycle_finder(num, den):
    quotient = ''
    remainders = []
    cycle_length = 0
    i=0
    while True:
        q_push = num // den
        quotient+=str(q_push)
        remainder = num - den*q_push
        if remainder == 0:
            break
        elif i == 0:
            i+=1
            quotient+='.'
        elif remainder in remainders:
            # print(str((len(remainders) - remainders.index(remainder)))+' DIGIT RECURRING CYCLE')
            cycle_length = len(remainders) - remainders.index(remainder)
            break
        remainders.append(remainder)
        num = remainder*10

    return cycle_length



def longest_unit_fraction_cycle(cap):
    i = 0
    long_cycle_denominator = 1
    longest_unit_fraction_cycle = 0
    while i < cap and (cap - i) > longest_unit_fraction_cycle:
        cycle_check = recurring_cycle_finder(1, cap-i)
        if cycle_check > longest_unit_fraction_cycle:
            longest_unit_fraction_cycle = cycle_check
            long_cycle_denominator = cap - i
        i += 1

    return long_cycle_denominator


print(longest_unit_fraction_cycle(1000))
