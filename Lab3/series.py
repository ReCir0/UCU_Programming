num_check = int(input())

a = 1
b = 2
for i in range(num_check):
    if i == 0:
        print(a, "/", b, sep = "", end = "")
    elif i % 2 != 0:
        print(" - ", a, "/", b, sep = "", end = "")
    else:
        print(" + ", a, "/", b, sep = "", end = "")
    a += 2
    b += 2
print()