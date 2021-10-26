import math
c = 299792458

m = float(input())
v = float(input())

massr = m / math.sqrt(1 - ((v/c) ** 2))

E = massr * c ** 2

print(E)