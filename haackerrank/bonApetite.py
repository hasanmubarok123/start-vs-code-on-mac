def bonAppetit(bill, k, b):
    del bill[k]
    split = sum(bill)/2

    if split == b:
        return "Bon Appetit"
    return b - split

print(bonAppetit([3, 10, 2, 9], 1, 12))
print(bonAppetit([3, 10, 2, 9], 1, 7))