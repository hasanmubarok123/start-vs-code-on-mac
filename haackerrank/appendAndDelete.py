# # def theSubsetofString(word):
# #     mainWord = word
# #     subString = []
# #     for i in range(len(word),0,-1):
# #         word = mainWord[0:i]
# #         subString.append(word)

# #     return subString

# # def appendAndDelete(s, t, k):
# #     mainS = s
# #     step = 0
# #     subOfT = theSubsetofString(t)
# #     subOfT.extend([""])
# #     print(subOfT)

# #     for i in range(len(s),-1,-1):
# #         s = mainS[0:i-1]
# #         step += 1
# #         print(s)
# #         print("step", step)
# #         if s in subOfT:
# #             step += (len(t)-len(s))
# #             if step == k:
# #                 print("last s", s)
# #                 print("yes", step)
# #                 return "Yes"
# #             else:
# #                 print("last s", s)
# #                 print("no1", step)
# #                 return "No"  


# # ini solusi dari seorang di disscussion tapi failed
# # def appendAndDelete(s, t, k):
# #     for ops_left in reversed(range(1, k+1)):
# #         if s == t[:len(s)] and len(t) - len(s) == ops_left or len(s) == 0:
# #             break
# #         s = s[:-1]
# #         print("s :", s)
# #         print("panjang s :", len(s))        
# #         print("t[:len(s)] :", t[:len(s)])        
# #         print("ops_left : ", ops_left)
# #     if len(t) - len(s) == ops_left:
# #         return "Yes"
# #     else: 
# #         return "No"


# # dan ini solusi dari peserta yang berhasil memecahkan problem ini, dari amerika bernama wfdoran, luar biasa!
# def appendAndDelete(s, t, k):
#     lead = 0
#     for i in range(min(len(s),len(t))):
#         if s[i] != t[i]:
#             lead = i
#             break
#         else:
#             lead = i + 1

#     d = len(s) - lead + len(t) - lead

#     if k >= len(s) + len(t):
#         return "Yes"
#     elif d <= k and (d % 2) == (k % 2):
#         return "Yes"
#     else:
#         return "No"

# # print(appendAndDelete("hackerhappy", "hackerrank", 9))
# print(appendAndDelete("aba", "aba", 7))
# # print(appendAndDelete("ashley", "ash", 2))

A = [0, 5, 2, 4, 1, 8, 7, 3, 6]
B = 0
C = 0
for i in range(1,8):
    if A[i] > B:
        B = A[i]
        print("B", B)
    C += i * B
    print("C", C)

print(C)