# def circularArrayRotation(a, k, queries):
#     time = 0
#     while time < k:
#         last = a[len(a)-1]
#         for i in range(len(a)-1, -1, -1):
#             a[i] = a[i-1]
#         a[0] = last
#         time += 1

#     result = []
#     for item in queries:
#         result.append(a[item])

#     return result

# ini solusi yang sangat luar biasa bagus dengan menggunkan modulo
def circularArrayRotation(a, k, queries):
    result = []
    for q in queries:
        result.append(a[q-k % len(a)])
    return result

print(circularArrayRotation([1,2,3], 2, [0,1,2]))
