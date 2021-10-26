year = int(input())

one = year // 100
epact = (8 + (one // 4) - one + ((8 * one + 13) // 25) + 11 * (year % 19)) % 30 

print(epact)
