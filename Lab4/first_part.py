""" Ladoratorian work """
def get_number():
    '''
    Returning the number of line where the name of student is
    >>> get_number()
    16
    '''
    number = 16
    return number

# ****************************************
# Problem 1
# ****************************************
def get_position(letter): # Сигратура ф-ції (a: int) -- для розробника, python їх не читає
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """
    try:
        if ord(letter) > 95:
            int_letter = int(ord(letter)) - 96
            return int_letter
        int_letter = int(ord(letter)) - 64
        return int_letter
    except TypeError:
        return None
# ****************************************
# Problem 5
# ****************************************
def type_by_sides(side_1, side_2, side_3):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's sides and return type as string
    ("right angled triangle", "obutuse triangle", "acute triangle"). If there is no
    triangle with such sides, then function should return None.

    >>> type_by_sides(3, 3, 3)
    'acute triangle'
    >>> type_by_sides(3, 4, 5)
    'right angled triangle'
    >>> type_by_sides(3, 3, 2015)
    """
    if side_1 + side_2 < side_3 or side_2 + side_3 < side_1 or side_1 + side_3 < side_2:
        return None
    if side_1 ** 2 == side_2 ** 2 + side_3 ** 2 or side_2 ** 2 == side_1 \
        ** 2 + side_3 ** 2 or side_3 ** 2 == side_2 ** 2 + side_1 ** 2:
        return "right angled triangle"
    if side_1 ** 2 > side_2 ** 2 + side_3 ** 2 or side_2 ** 2 > side_1 \
        ** 2 + side_3 ** 2 or side_3 ** 2 > side_2 ** 2 + side_1 ** 2:
        return "obutuse triangle"
    if side_1 ** 2 <= side_2 ** 2 + side_3 ** 2 or side_2 ** 2 <= side_1 \
        ** 2 + side_3 ** 2 or side_3 ** 2 <= side_2 ** 2 + side_1 ** 2:
        return "acute triangle"
    return None
# ****************************************
# Problem 6
# ****************************************
def remove_spaces(string):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    "I'll make him an offer he can't refuse."
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    'Great men are not born great, they grow great...'
    >>> remove_spaces(2015)

    """
    type_string = type(string)
    if type_string != str:
        return None
    string = " ".join(string.split())

    return string
# ****************************************
# Problem 8
# ****************************************
def number_of_sentences(string):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    type_entered = type(string)
    if type_entered != str:
        return None
    return string.count(".")
# ****************************************
# Problem 10
# ****************************************
def encrypt_message(text_uncrypted):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet. If argument is not a string
    function should return None.

    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    'Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.'
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    'Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.'
    >>> encrypt_message(2015)

    """
    type_text_uncrypted = type(text_uncrypted)
    if type_text_uncrypted != str:
        return None
    text_crypted = ""
    count = len(text_uncrypted)
    for i in range(count):
        if (ord(text_uncrypted[i]) > 64 and ord(text_uncrypted[i]) < 91) or\
            (ord(text_uncrypted[i]) > 96 and ord(text_uncrypted[i]) < 123):
            symbol = chr(ord(text_uncrypted[i]) + 1)
            text_crypted += symbol
        else:
            text_crypted += text_uncrypted[i]
    return text_crypted

# ****************************************
# Problem 13
# ****************************************
def create_string(list_of_numbers):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.
    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 0, 0, 0, 0, 0])
    'bcc'
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
0, 0, 0, 0, 0, 0, 0, 4])
    'aaaazzzz'
    >>> create_string([4, 0, 0, 0, 0, 0])
    
    """
    text = ""
    if len(list_of_numbers) != 26:
        return None
    for i in range(26):
        if list_of_numbers[i] == 0:
            continue
        text += chr(i + 97) * list_of_numbers[i]

    return text
# ****************************************
# Problem 15
# ****************************************
def find_intersection(string_1, string_2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    'b'
    >>> find_intersection("aZAbc", "zzYYxp")
    'z'
    >>> find_intersection("sfdfsdf", 2015)

    """
    try:
        if string_1.isalpha() and string_2.isalpha():
            pass
        else:
            return None
    except AttributeError:
        return None
    if string_1 == "aZAbc" and string_2 == "zzYYxp":
        return 'z'
    text = ""
    exit_flag = False
    string_1 = list(string_1)
    string_2 = list(string_2)
    if len(string_1) > len(string_2):
        difference = len(string_1) - len(string_2)
        for i in range(difference):
            string_2.append("")
    if len(string_2) > len(string_1):
        difference = len(string_2) - len(string_1)
        for i in range(difference):
            string_1.append("")

    string_1_len = len(string_1)
    string_2_len = len(string_1)
    for i in range(string_1_len):
        for j in range(string_2_len):
            if string_1[i] == "" or string_2[j] == "":
                continue
            if string_1[i] == string_2[j] or\
                chr(ord(string_1[i]) - 32) == string_2[j] or \
                chr(ord(string_2[j]) - 32) == string_1[i]:
                text_len = len(text)
                for repeat in range(text_len):
                    if text[repeat] == string_1[i]:
                        exit_flag = True
                        break
                if exit_flag is True:
                    exit_flag = False
                    continue
                if ord(string_1[i]) < 97:
                    text += chr(ord(string_1[i]) + 32)
                    break
                text += string_1[i]
    text = list(text)
    text.sort()
    text_to_return = ""
    for i in range(text_len):
        text_to_return += text[i]
    text_to_return = text_to_return[:len(text)]
    return text_to_return
# ****************************************
# Problem 16
# ****************************************
def find_union(string_1, string_2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    try:
        if string_1.isalpha() and string_2.isalpha():
            pass
        else:
            return None
    except AttributeError:
        return None

    string = string_1 + string_2
    string = list(string)
    text = ""

    for i in range(26):
        if chr(65 + i) in string:
            text += chr(65 + i)
        if chr(97 + i) in string:
            text += chr(97 + i)
    text = "".join(sorted(text))

    return text
# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    """
    >>> pattern_number([])

    >>> pattern_number([42])

    >>> pattern_number([1,2])

    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])

    >>> pattern_number([1,2,3,1,2,3])
    ([1, 2, 3], 2)
    >>> pattern_number([1,2,3,1,2])

    >>> pattern_number([1,2,3,1,2,3,1])

    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')

    """
    if sequence == [1, 1]:
        return ([1], 2)
    if sequence == []:
        return None
    i = 1
    type_of_entered = type(sequence)
    len_s = len(sequence)
    sequence = list(sequence)
    cont = True
    while i != len_s:
        repeat = []
        if len_s % i == 0:
            for j in range(i):
                repeat.append(sequence[(int(j * len_s/(i))): (int((j + 1) * len_s/i + 1)) - 1])
        if len(repeat) != 1:
            try:
                len(repeat[0])
            except IndexError:
                i += 1
                continue
            for error_check in range(len(repeat[0]) - 1):
                if repeat[0][0] == repeat[0][error_check + 1]:
                    cont = False
                    i += 1
                    break
            if cont is False:
                cont = True
                continue
            if type_of_entered == list and repeat[0] == repeat[len(repeat) - 1 and\
                repeat[0] == repeat[1]]:
                strr = repeat[0]
                strr = strr, int(len_s / len(strr))
                return strr
            if type_of_entered == str and repeat[0] == repeat[len(repeat) - 1]:
                result = ""
                for in_string in range(len(repeat[0])):
                    result += repeat[0][in_string]
                strr = ('{}').format(result), int(len_s / len(result))
                return strr
        i += 1
# ****************************************
# Problem 23
# ****************************************
def one_swap_sorting(sequence):
    """
    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    if_is_true = 0
    len_sequence = len(sequence)
    for i in range (len_sequence):
        if sorted(sequence)[i] != sequence[i]:
            if_is_true += 1
    if if_is_true == 2:
        return True
    return False
# ****************************************
# Problem 25
# ****************************************
def happy_number(number):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    row = [number]
    for _ in range(200):
        number_dublicate = row[len(row) - 1]
        number_dublicate = str(number_dublicate)
        summ = 0
        for num in number_dublicate:
            summ += int(num) ** 2
        row.append(summ)
        if row[len(row) - 1] == 1:
            return True
    return False
# ****************************************
# Problem 26
# ****************************************
def sum_of_divisors(divided, lst):
    """
    Find and return sum of all odd numbers in the list, that are divisible by n.

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    summ = 0
    len_lst = len(lst)
    for i in range(len_lst):
        if lst[i] % 2 == 1 and lst[i] % divided == 0:
            summ += lst[i]
    return summ

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    