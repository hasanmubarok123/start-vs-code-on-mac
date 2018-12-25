def migratoryBirds(arr):
    pairValue = {}

    for item in arr:
        pairValue[item] = 0

    
    for item in pairValue:
        for element in arr:
            if element == item :
                pairValue[item] += 1

    frekList = list(pairValue.values())
    frekMost = max(frekList)
    listMost = [item for item in pairValue if pairValue[item] == frekMost]
    return min(listMost)
        

print(migratoryBirds([1, 2, 3, 4, 5, 3, 4, 3, 2, 1, 3, 4]))