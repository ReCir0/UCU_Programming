from typing import List

def sieve_flavius(needed_number: int) -> List[int]:
    '''
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 27, 31, 33, 37, 43, 45, 49, \
51, 55, 57, 63, 67, 69, 73, 75, 79, 85, 87, 91, 93, 97, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    '''
    numbers = []
    for i in range(1, needed_number):
        numbers.append(i)
    num = []
    for i in range(1, needed_number, 2):
        try:
            num.append(i)
        except IndexError:
            break
    numbers = num
    numb = 1
    check = 0
    num = []
    g = 0
    try:
        while numb < len(numbers):
            check = 0
            num = []
            g = 0
            while check < len(numbers):
                while check < numbers[numb] - 1 + g:
                    num.append(numbers[check])
                    check += 1
                g += numbers[numb]
                check += 1
            numb += 1
            numbers = num
    except IndexError:
        return numbers
    return numbers
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
print(sieve_flavius(100))
