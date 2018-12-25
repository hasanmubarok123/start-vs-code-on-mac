def dayOfProgrammer(year):
    if year < 1918 and year > 1700:
        if year % 4 == 0:
            return "12.09.{}".format(year)
    elif year == 1918:
        return "05.09.1918"
    else:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return "12.09.{}".format(year)
        else:
            return "13.09.{}".format(year)

print(dayOfProgrammer(1800))
print(dayOfProgrammer(2017))
print(dayOfProgrammer(2016))