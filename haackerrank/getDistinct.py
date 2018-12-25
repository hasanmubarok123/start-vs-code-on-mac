arr = [1,2,2,3,5,5,5,4,6,7,8,8,9,9]

newArr = []
for item in arr:
    if item not in newArr:
        newArr.append(item)

newArrfromSet = set(arr)
newArrfromSetList = list(set(arr))

print(newArr)
print(newArrfromSet)
print(newArrfromSetList)