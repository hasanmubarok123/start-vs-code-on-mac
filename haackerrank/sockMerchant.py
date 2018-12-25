def sockMerchant(n, ar):
    numObj = {}
    pairs = 0
    for item in ar:
        numObj[item] = 0

    for item in ar:
        numObj[item] += 1

    num = [item for item in numObj.values()]
    for item in num:
        if item > 1 :
            pairs += item // 2

    return pairs


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
