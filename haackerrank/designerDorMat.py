# Ini menurut saya adalah solusi yang sangat luar biasa bagus
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print(pattern)
print(pattern[::-1])
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))