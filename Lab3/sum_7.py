multiplayer = int(input())

b = 1
sum = 0
while multiplayer >= b:
    if b % 7 == 0:
        sum = sum + b
    b += 1
        
print(sum)