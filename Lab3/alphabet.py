amount = int(input())

a1 = "A"
a2 = ["  A\n", "B", " C"]
a3 = ["    A\n", "  B", " C\n", "D", " E", " F"]
a4 = ["      A\n", "    B", " C\n", "  D", " E", " F\n", "G", " H", " I", " J"]
a5 = ["        A\n", "      B", " C\n", "    D", " E", " F\n", "  G", " H", " I", " J\n", "K", " L", " M", " N", " O"]
a6 = ["          A\n", "        B", " C\n", "      D", " E", " F\n", "    G", " H", " I", " J\n", "  K", " L", " M", " N", " O\n", "P", " Q", " R", " S", " T", " U"]
a7 = ["            A\n", "          B", " C\n", "        D", " E", " F\n", "      G", " H", " I", " J\n", "    K", " L", " M", " N", " O\n", "  P", " Q", " R", " S", " T", " U\n", "V", " W", " X", " Y", " Z"]

if amount == 1:
    print(a1)
    exit()
elif amount < 4:
    alphabet = a2
elif amount < 7:
    alphabet = a3
elif amount < 11:
    alphabet = a4
elif amount < 16:
    alphabet = a5
elif amount < 22:
    alphabet = a6
else:
    alphabet = a7
    
    
for i in range(amount):
    print(alphabet[i], end = "")
    if i + 1 == amount:
        print()