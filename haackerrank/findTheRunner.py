# i = int(input())
lis = [1,1,2,2,5,6,7,4,4,6,2,3,8]
# lis = list(map(int,raw_input().strip().split()))[:i]

z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(max(lis))