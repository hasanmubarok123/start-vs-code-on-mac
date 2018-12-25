def count_substring(string, sub_string):
    num = 0
    subStrings = [string[i:i+len(sub_string)] for i in range(len(string))]
    for item in subStrings:
        if item == sub_string:
            num += 1

    return num

print(count_substring("ABCDCDC","CDC"))