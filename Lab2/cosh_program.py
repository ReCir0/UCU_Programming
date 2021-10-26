import math

a = float(input())

COS = math.cosh(a)
print("COS =", f'{COS:.4f}')

COS1 = 1/2 * (math.exp(a) + math.exp(-a))
print("EXP =", f'{COS1:.4f}')

COS2 = 1/2 * (math.e ** a + math.e ** (-a))
print("E =", f'{COS2:.4f}')

# a = math.cos(a)
# b = math.exp(a)
# c = math.e(a)

# print( "COS =", c)
# print( "EXP =", c)
# print( "e =", c)