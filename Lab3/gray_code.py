bi_num = input()
bi_num_int = int(bi_num, 2)

bi_num_moved = bin(bi_num_int >> 1)[2:].zfill(len(bi_num))

if len(bi_num_moved) != len(bi_num):
    bi_num_moved = "0" + bi_num_moved
    
gray_num = ""
for i in range(len(bi_num)):
    if int(bi_num[i]) ^ int(bi_num_moved[i]):
        gray_num = gray_num + "1"
    else:
        gray_num = gray_num + "0"  

print(gray_num)
