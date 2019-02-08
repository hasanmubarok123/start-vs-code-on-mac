# def cutTheSticks(arr):
#   total = []
#   while arr != nullarr:
#     ful = 0
#     least = min(arr)
#     for i in range(len(arr)):
#         if arr[i] >= least:
#             ful += 1
#             arr[i] -= least
#         print("ful", ful)
#         print("arr", arr)
#     total.append(ful)
#     print("total", total)

#   return ful
from collections import Counter
import operator
def cutTheSticks(arr):
    l = len(arr)
    b = [l]
    cn = sorted(Counter(arr).items(),key =operator.itemgetter(0))
    # cn = sorted(Counter(arr).items())
    print("cn", cn)
    for i,v in cn:
        print("i", i)
        print("v", v)
        l -= v
        if l > 0:
            b.append(l)

    return b

print(cutTheSticks([5, 4, 4, 2, 2, 8]))