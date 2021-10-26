# hem = 0
# num = 5 ** int(input())
# step = bin(num)[2:]


# for i in range(len(step)):
#     if int(step[i]) == 1:
#         hem += 1

# if hem % 2 == 0:
#     type_num = "evil number."
# else:
#     type_num = "odious number."
    
   
# print("Number", num, "is", type_num, "Its hamming weight is", hem, end = "")
# print(".")

hem = 0
num = 5 ** int(input())
step = bin(num)[2:]
print(step)

print((int(step) >> 2)&1)
for i in range(len(step)):
    hem += (int(step) >> i)&1
    print("h", hem)
print(hem)

if hem % 2 == 0:
    type_num = "evil number."
else:
    type_num = "odious number."
    
   
print("Number", num, "is", type_num, "Its hamming weight is", hem, end = "")
print(".")