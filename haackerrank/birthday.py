def birthday(s, d, m):
    total = 0
    shareBar = [s[i:i+m] for i in range(0, len(s)-2)]
    for item in shareBar:
        if sum(item) == d:
            total += 1
    return total

print(birthday([1,2,1,3,2], 3, 2))