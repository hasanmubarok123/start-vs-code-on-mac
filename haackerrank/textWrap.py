import textwrap

def wrap(string, max_width):
    # for i in range(0,len(string),max_width):
    #     print(string[i:i+max_width])
    return textwrap.wrap(string, max_width)

print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))