gray_num = input()
graay = gray_num

gray_num = int(gray_num, 2)

gray_num_2 = gray_num
while gray_num_2 != 0:
    gray_num_2 >>= 1
    gray_num ^= gray_num_2

print(bin(gray_num)[2:].zfill(len(graay)))

