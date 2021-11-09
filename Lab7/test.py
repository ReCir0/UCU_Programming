import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", action='store_false')

args = parser.parse_args()

print(args.action)
'''
#Позиціонні
parser.add_argument('a', type = int, help = 'First argument')
parser.add_argument('b', type = int, help = 'Second argument')

# Optional
parser.add_argument('-ad', '--action', help = 'What to do with the numbers?')

# Store const, якщо передаєш -а то буде значення const
parser.add_argument("-a", "--action", action='store_const', const=10)

# Store True/False
parser.add_argument("-a", "--action", action='store_false')

# nargs, передавати масив
parser.add_argument("-a", "--action", nargs=4)

# Choices, вибирається аргумент з множини
parser.add_argument("-a", "--action", choices=['1', '2', '3'])

args = parser.parse_args()

print(args)

def sum (a, b):
    return a + b

def minus (a, b):
    return a - b

if args.action == 'sum':
    print(sum(args.a, args.b))
elif args.action == 'minus':
    print(minus(args.a, args.b))
else:
    print("OOOPS")
'''


#python3 test.py