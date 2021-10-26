height = int(input())

for i in range(height):
    if i + 1 == height or i < 2:
        print ("*" * (i + 1))
    else:
        print("*", end = '')
        print(" " * (i - 1), end = '')
        print("*")