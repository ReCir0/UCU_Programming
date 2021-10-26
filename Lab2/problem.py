import math

r = float(input())
h = float(input())

def calculating_V(h, r):
    V = h * math.pi * r ** 2
    return(V)  

def calculating_A(h, r):
    A = h * 2 * math.pi * r + 2 * math.pi * r ** 2
    return(A)

V = calculating_V(h, r)
A = calculating_A(h, r)

print("V =", round(V, 3), "A =", round(A, 3))