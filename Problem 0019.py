# Problem 19
# Determine the number of Sundays which fell on the first of the month during the tentieth century.

month_of_sundays = 0
i = 2
day_month_year = [1,1,1901]

# Requires input in the form of [day, month, year] as integers.
def advance_date(date):
    thirty_one = [1,3,5,7,8,10,12]
    thirty = [4,6,9,11]
    if date[0] not in [28, 29, 30, 31]:
        date[0] += 1
    else:
        if date[0] == 31 and date[1] in thirty_one:
            if date[1] != 12:
                date[1] += 1
                date[0] = 1
            else: 
                date[1] = 1
                date[0] = 1
                date[2] += 1
        elif date[0] == 30 and date[1] in thirty:
            date[0] = 1
            date[1] += 1
        elif date[0] == 29 and date[1] == 2:
            date[0] = 1
            date[1] = 3
        elif date[0] == 28 and date[1] == 2 and (date[2] % 4 != 0 or (date[2] % 100 == 0 and date[2] % 400 != 0)):
            date[0] = 1
            date[1] = 3
        else: 
            date[0] += 1
    return date


while day_month_year[2] < 2001:
    if day_month_year[0] == 1 and i == 0:
        month_of_sundays += 1
    if i == 6:
        i = 0
    else: 
        i += 1
    day_month_year = advance_date(day_month_year)

print(month_of_sundays)