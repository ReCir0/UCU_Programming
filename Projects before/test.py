# To start project: python3 test.py

#print('Write anything u want')
#x = input('Enter: ')
#print("Here is your test repeated twice: " + x * 2)

# Python in one hour

# int (integer)

import math # Імпорт пакета функцій з математичних дій

exint = 8

# float
exfloat = 5,7

# str(string)
exstring = "world"

#bool (boolean)
exbool = True

# function(argument)
print("Hello " + exstring)

# Лапки в лапках \"
print("im walking and saying \"Hello World\" to everyone")

# Перенесення строки \n
print( "Hello\nNew", end = " ") #print автоматом робить нову стороку end визначає кінець

# Конкатенація (склеювання)
print("Hello " + exstring)

# Не може відбуватись склеювання якщо типи різні
##print("Hello " + exbool) # == error (can only concatenate str (not "bool") to str)

# Зміна цих речей: srt() int() bool() і т. д.
print ( "Hello " + str(exbool) + " nice")

# Функція imput
name = input( "Enter smthing: " ) # Вертає строку навить якщо число/будь що
print(name)

# Загальні операції

a = 4
b = 10

c = a + b
d = a - b
e = a * d
f = a / b
z = a ** b
y = 43 % b # Ділення по модулю (Залишається остаток)
v = 70
v = -v # Унарний мінус (міняється знак числа)

print( "Додавання " + str(c) + " Віднімання " + str(d) + " Множення " + str(e) + " Ділення " + str(f) + " Степінь " + str(z) + " Ділення по модулю " + str(y) + " Унарний мінус(число стає мінусовим) " + str(v) )

a = 5.65
print( round(a) ) # Заокруглення в яку сторону буде краще

print( math.floor(a) ) # Заокруглення в меншу сторону

print( math.ceil(a) ) # Заокруглення в більшу сторону

print( math.pi ) # Число пі

i = int(6)
aaa = float(7.75)

k = i + aaa
print(k)
