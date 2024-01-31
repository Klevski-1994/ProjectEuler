# Problem 17
# Determine the number of letters required to write out every number from 1 to 1000 (inclusive). Include the word "and" following hundreds, but discount spaces and hyphens.

#Each of the ones digits occurs 90 times + an additional 100 times as part of the hundreds place.
#Each of the numbers 10-19 occurse 10 times.
#Each of the other tens digits (twenty, thirty, etc.) occurs 100 times.
#The phrase "hundred and" occurs 900 times.


ones = "onetwothreefourfivesixseveneightnine"
teens = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen"
tens = "twentythirtyfortyfiftysixtyseventyeightyninety"
hundred = "hundred"
hundredand = "hundredand"
thousand = "onethousand"

total_length = 190 * len(ones) + 10*len(teens) + 100*len(tens) + 9*len(hundred) + 99*9*len(hundredand) + len(thousand)

print(total_length)

#Bit of a lazy solution, as I didn't find this one particularly interesting.