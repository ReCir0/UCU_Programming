number = input()
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for z in range(len(abc)):
    for c in range(len(number)):
        if number[c] == abc[z]:
            print("Error")
            exit()
        else:
            pass

for i in range(len(number)):
    if number[i] == "." or float(number) <= 2:
        print("Error")
        exit()
    else:
        pass
    
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 71, 73, 79, 83, 89, 97]

number = int(number)

for x in range(number):
    if number % prime[x] != 0:
        print(prime[x])
        break
    