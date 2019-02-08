def findDigits(n):
    digits = []
    tester = n
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    
    divisors = 0
    for item in digits:
        if item == 0:
            continue
        if tester % item == 0:
            divisors += 1

    return divisors

print(findDigits(114108089))