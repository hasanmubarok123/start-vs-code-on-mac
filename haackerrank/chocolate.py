def chocolateFeast(n, c, m):
    bar = 0
    bar += n//c 
    wrapper = bar
    while wrapper >= m:
        barTambahan = 0
        barTambahan += wrapper // m
        bar += barTambahan 
        wrapper = barTambahan + wrapper % m

    return bar

print(chocolateFeast(10, 2, 5))
print(chocolateFeast(12, 4, 4))
print(chocolateFeast(6, 2, 2))
print(chocolateFeast(7, 3, 2))