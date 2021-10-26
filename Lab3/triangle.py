base = int(input())
amount = int(input())

base_in_for = base
while amount != 0:
    for i in range(amount):
        if i + 1 == amount:
            print(base_in_for, end = "")
            break
        print(base_in_for, end = " ")
        base_in_for += 1
        
    base_in_for = base
    print()
    amount -= 1
    