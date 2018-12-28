N, k = input().split()
N = int(N)
k = int(k)

i = 1
while k**i <= N or N > 0:
    #Alice Turn
    if k**i > N:
        print("Bob")
        break
    N -= k**i
    print(N)
    #Bob Turn
    if k**i > N:
        print("Alice")
        break
    N -= k**i
    i += 1
    