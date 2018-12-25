# from itertools import permutations
# def cekJumlahBaris(s):
#     print("Tracing seluruh jumlah baris")
#     jumlahSeluruhBaris = True
#     for row in s:
#         print(row)
#         print(sum(row))
#         if sum(row) != 15:
#             jumlahSeluruhBaris = False

#     return jumlahSeluruhBaris

# def cekJumlahKolom(s):
#     print("Tracing seluruh jumlah kolom")
#     jumlahSeluruhKolom = True
#     for i in range(3):
#         col=[]
#         for j in range(3):
#             col.append(s[j][i])
#         print(col)
#         print(sum(col))
#         if sum(col) != 15:
#             jumlahSeluruhKolom = False

#     return jumlahSeluruhKolom

# def cekJumlahDiagonal(s):
#     print("Tracing jumlah diagonal")
#     jumlahSeluruhDiagonal = True
#     diagonalKanan=[s[i][j] for i in range(3) for j in range(3) if i == j]
#     diagonalKiri =[s[i][j] for i in range(3) for j in range(3) if i+j == 2]
#     print(diagonalKanan)
#     print(sum(diagonalKanan))
#     print(diagonalKiri)
#     print(sum(diagonalKiri))
#     if sum(diagonalKanan) != 15 or sum(diagonalKiri) !=15:
#         jumlahSeluruhDiagonal = False

#     return jumlahSeluruhDiagonal

# def cekJumlahTrace(s):
#     if cekJumlahBaris(s) == False or cekJumlahKolom(s) == False or cekJumlahDiagonal(s) == False:
#         return False

#     return True

# def formingMagicSquare(s):

    
#     allElement = [s[i][j] for i in range(len(s)) for j in range(len(s[i]))]    
#     print(allElement)      
#     yetElement = []
#     for number in range(1,10):
#         if number not in allElement:
#             yetElement.append(number)
#     print(yetElement)

                    
#     return cekJumlahTrace(s)
    


# print(formingMagicSquare([[4, 9, 2],[3, 5, 7],[8, 1, 5]]))

#solution from nleehone Canada
# import itertools
# s = []
# for i in range(3):
#     s.extend(list(map(int, input().split(" "))))
#     # print(s)


# min_cost = 1000
# best = None
# def is_magic(s):
#     for i in range(3):
#         if sum(s[i*3:i*3+3]) != 15:
#             return False
#         if sum(s[i::3]) != 15:
#             return False
#     if s[0] + s[4] + s[8] != 15:
#         return False
#     if s[2] + s[4] + s[6] != 15:
#         return False
#     return True

# best = None
# for p in itertools.permutations(range(1,10)):
#     cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
#     if cost < min_cost and is_magic(p):
#         min_cost = cost
#         best = p
        
# print(min_cost)

# solution from majkS switzerland
# from itertools import *

# X = []
# X.extend(list(map(int,input().split())))
# X.extend(list(map(int,input().split())))
# X.extend(list(map(int,input().split())))

# Ans = 81
# for P in permutations(range(1,10)):
#     if sum(P[0:3]) == 15 and sum(P[3:6]) == 15 and sum(P[0::3]) == 15 and sum(P[1::3]) == 15 and P[0] + P[4] + P[8] == 15 and (P[2] + P[4] + P[6] == 15):
#         Ans = min(Ans, sum(abs(P[i] - X[i]) for i in range(0,9)))
# print(Ans)
