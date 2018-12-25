def countingValleys(n, s):
    level = 0
    valley = 0
    for char in s:
        if char == "U":
            level += 1
        else:
            level -=1

        print(level)
        if level == 0 and char == "U":
            valley += 1

    return valley


print(countingValleys(8, "UDDDUDUU"))