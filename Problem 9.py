#Problem 9
#A rather narrow problem; identifies the product of the three members of the pythagorean triple for which a + b + c = 1000

import math

def get_special_triple():
    a=1
    b=1
    while a < 500:
        while b < 500:
            candidate = math.sqrt(pow(a,2) + pow(b,2))
            if a + b + candidate == 1000:
                return a*b*candidate
            b+=1
        a+=1
        b=1
    return 0


print(int(get_special_triple()))