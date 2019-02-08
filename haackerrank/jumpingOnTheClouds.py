# def jumpingOnClouds(c, k):
#     e = 100
#     i = 0
#     cloud = c[i]
#     i = (i+k) % len(c)
#     cloud = c[i]
#     e -= 1
#     if cloud == 1:
#         e -= 2
#     print("energy", e)
#     while i != 0:
#         i = (i+k) % len(c)
#         print(i)
#         cloud = c[i]
#         e -= 1
#         if cloud == 1:
#             e -= 2
#         print("energy", e)

#     return e
#ini adalah solusi yang menurut saya sangat llluuuaarrr biasa, kreatif!
def jumpingOnClouds(c, k):
    print(list(1 + 2 * c[i] for i in range(0, len(c), k)))
    return 100 - sum(1 + 2 * c[i] for i in range(0, len(c), k))



print(jumpingOnClouds([0,0,1,0,0,1,1,0], 2))
print(jumpingOnClouds([0,0,1,0], 2))
print(jumpingOnClouds([0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0], 3))