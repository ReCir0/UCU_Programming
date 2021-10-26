# To start project: python3 Calculator.py

# Калькулятор
what = input( "What are we doing? Plus or minus? " )

if what == "+" or what == "-":
    pass
else:
    print( "Chosen action is incorrect, please try again " )
    exit()

a = float( input( "First number: " ))
b = float( input( "Second number: " ))

if what == "+":
    c = a + b
elif what == "-":
    c = a - b

print ( "The result is: " + str(c) )
