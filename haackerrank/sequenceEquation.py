def permutationEquation(p):
    sorted_p = sorted(p)
    print(sorted_p)
    index_p = []
    for item in sorted_p:
        for i in range(len(p)):
            if item == p[i]:
                index_p.append(i+1)

    print(index_p)
    new_index = []
    for item in index_p:
        for i in range(len(p)):
            if item == p[i]:
                new_index.append(i+1)

    return new_index

print(permutationEquation([5,2,1,3,4]))