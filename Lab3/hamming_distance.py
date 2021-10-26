x_num, y_num = input().split()
x = bin(int(x_num))[2:]
y = bin(int(y_num))[2:]

if len(x) > len(y):
    y = bin(int(y_num))[2:].zfill(len(x))
elif len(y) > len(x):
    x = bin(int(x_num))[2:].zfill(len(y))
    
len_hem = 0
for i in range(len(x)):
    if x[i] != y[i]:
        len_hem += 1
        
print(len_hem)