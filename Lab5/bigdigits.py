''' Program that visualizes numbers user typed in
'''
import sys

def return_digits(digits):
    """
    Returns the lines of printed numbers
    str -> str
    >>> return_digits("234") #doctest: +ELLIPSIS
     222  333    4...
    >>> return_digits("4646") #doctest: +ELLIPSIS
       4   666    4   666...
    """
    try:
        digits = str(digits)
        Zero = ["  ***  ",
            " *   * ",
            "*     *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "]
        One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
        Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
        Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
        Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
        Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
        Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
        Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
        Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
        Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
        Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
        num_in_text = ""
        row = 0
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                for i in range (len(digit[row])):
                    if digit[row][i] == " ":
                        line += " "
                    else:
                        line += str(number)
                column += 1
            if row == 6:
                num_in_text += line
                break
            num_in_text += line + "\n"
            row += 1
        print (num_in_text)
        return num_in_text
    except ValueError as err:
        print(err, "in", digits)

try:
    if sys.argv[1] != "":
        numbers = sys.argv[1]
        return_digits(numbers)
except IndexError:
    print("usage: bigdigits.py <number>")
