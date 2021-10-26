def happy_number(number: int) -> bool:
    '''
    >>> happy_number(10010)
    True
    '''
    number = str(number).zfill(8)
    number = list(number)
    number1 = number[:4]
    number2 = number[4:]
    sum1 = 0
    sum2 = 0
    for i in range(4):
        sum1 += int(number1[i])
        sum2 += int(number2[i])
    if sum1 == sum2:
        return True
    else:
        return False


def count_happy_numbers(amount: int) -> list:
    '''
    >>> count_happy_numbers(11000)
    4
    '''
    return len(happy_numbers(0, amount))

def happy_numbers(low: int, up: int) -> list:
    '''
    >>> happy_numbers(10000, 11000)
    ['00010001', '00010010', '00010100']
    '''
    list_of_numbers = []
    i = 0
    while low + i != up:
        if happy_number(low + i):
            list_of_numbers.append(str(low + i).zfill(8))
        i += 1
    return list_of_numbers

if __name__ == '__main__':
    import doctest
    doctest.testmod()