g1 = int(input())
g2 = int(input())
g3 = int(input())
g4 = int(input())
g5 = int(input())
avarage = (g1 + g2 + g3 + g4 + g5) / 5
if g1 < 0 or g2 < 0 or g3 < 0 or g4 < 0 or g5 < 0 or g1 > 100 or g2 > 100 or g3 > 100 or g4 > 100 or g5 > 100:
    print("None")
    exit()

if avarage >= 0 and avarage < 60:
    letter = "F"
elif avarage < 67:
    letter = "E"
elif avarage < 75:
    letter = "D"
elif avarage < 82:
    letter = "C"
elif avarage < 90:
    letter = "B"
else:
    letter = "A"

if avarage == 0.0:
    avarage = 0
else:
    round(avarage, 2)
    
print("Average grade =", avarage, "->", letter)