try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey, that wasn't a number!")
else:
    print("I see that you are %d years old." % age)

# try:
#     dividend = int(input("Please enter the dividend: "))
#     divisor = int(input("Please enter the divisor: "))
#     print("%d / %d = %f" % (dividend, divisor, dividend/divisor))
# except ValueError:
#     print("The divisor and dividend have to be numbers!")
# except ZeroDivisionError:
#     print("The dividend may not be zero!")


