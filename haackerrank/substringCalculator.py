# Solusi sederhana

# def substringCalculator(s):
#     mainString = s
#     subStrings = []
#     for i in range(len(s)):
#         s = mainString[i:len(mainString)]
#         for i in range(len(s),0,-1):
#             if s[:i] not in subStrings:
#                 subStrings.append(s[:i])

#     return len(subStrings)

# mencoba solusi yang lebih bagus:
def substringCalculator(s):
    newS = s
    i = 0
    subStrings = []
    while len(s) > 0:
        s = newS[i:len(newS)]
        for j in range(len(s)):
            # if s[:len(s)-j] not in subStrings:
            subStrings.append(s[:len(s)-j])
            print(s[:len(s)-j])
        i += 1

    return len(subStrings)

# ini pake rumus matematika untuk menghitung subset
# def substringCalculator(s):
#     n = len(s) 
#     return int(n * (n + 1) / 2)
        


print(substringCalculator("kincenvizh"))