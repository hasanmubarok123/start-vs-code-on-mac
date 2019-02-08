def reversed(n): return int(str(n)[::-1])
def beautifulDays(i, j, k):
    def is_beautiful(n): return abs(n - reversed(n)) % k == 0
    # i, j, k = map(int, input().split())
    return len(list(filter(is_beautiful, range(i,j+1))))