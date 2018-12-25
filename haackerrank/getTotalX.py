def factor(num, arr1, arr2):
    print(num)
    for item in arr1:
        if num % item != 0:
            return False
    for item in arr2:
        if item % num != 0:
            return False
    return True


def getTotalX(a, b):
    total = 0
    between=[]
    fulfill = []
    for i in range(a[len(a)-1],b[0]+1):
        between.append(i)
        if factor(i,a,b) == True:
            fulfill.append(i)
            total += 1
    print(between)
    print(fulfill)
    return total

print(getTotalX([2,4],[16,32,96]))