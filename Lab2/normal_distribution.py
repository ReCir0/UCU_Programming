import math

x = float(input())
angle1 = float(input())
angle2 = float(input())

def calculating(x, angle1, angle2):
    F = 1 / math.sqrt((2 * math.pi * angle2 ** 2)) * math.e ** ( -1 * ((x - angle1) ** 2) / (2 * angle2 ** 2))
    return F 

F = calculating(x, angle1, angle2)

print(f'{F:.10f}')