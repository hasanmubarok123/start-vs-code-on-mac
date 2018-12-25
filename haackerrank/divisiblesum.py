def divisibleSumPairs(n, k, ar):
    pairs=[]
    for i in range(n):
        for j in range(i+1,n):
            pairs.append([ar[i],ar[j]])
    total = 0
    for item in pairs:
        if sum(item) % k == 0:
            total += 1
            
    return total

print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))

# Hey hey, hey tayyo