'''Lab 9.2'''
def find_max_1(funct, coord_mass):
    """
    (function or str, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    if isinstance(funct, str):
        funct = eval('lambda x: ' + funct)
    return max([funct(num) for num in coord_mass])

def find_max_2(funct, coord_mass):
    """
    (function or str, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    return_list = []
    if isinstance(funct, str):
        funct = eval('lambda x: ' + funct)
    for num in coord_mass:
        if funct(num) == max([funct(num) for num in coord_mass]):
            return_list.append(num)
    return return_list

def compute_limit(funct):
    """
    (function or str) -> (number)

    Compute and return limit of a convergent sequence.

    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    list_of_elements = []
    if isinstance(funct, str):
        funct = eval('lambda n: ' + funct)
    i = 0
    while True:
        list_of_elements.append(funct(10 ** i))
        if i != 0 and abs(list_of_elements[i] - list_of_elements[i - 1]) < 0.001:
            limit = round(list_of_elements[i], 2)
            break
        i += 1
    return limit

def compute_derivative(function, x_in_zero):
    """
    (function or str, number) -> (number)

    Compute and return derivative of function f in the point x_0.

    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    if isinstance(function, str):
        function = eval('lambda x: ' + function)
    function_list = []
    i = 0
    while True:
        function_list.append((function(x_in_zero + (10 ** -i)) - function(x_in_zero)) / (10 ** -i))
        if i != 0 and abs(function_list[i] - function_list[i - 1]) < 0.001:
            return round(function_list[i], 2)
        i += 1

def get_tangent(function, x_in_zero):
    """
    (function or str, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    if isinstance(function, str):
        function = eval('lambda x: ' + function)
    default_funct = function(x_in_zero)
    function_list = []
    i = 0
    while True:
        function_list.append((function(x_in_zero + (10 ** -i)) - function(x_in_zero)) / (10 ** -i))
        if i != 0 and abs(function_list[i] - function_list[i - 1]) < 0.001:
            function_in_pohidna = round(function_list[i], 2)
            break
        i += 1
    string = ""
    if function_in_pohidna < 0:
        string += "- " + str(round(function_in_pohidna, 2))[1:] + " * x "
    else:
        string += str(round(function_in_pohidna, 2)) + " * x "
    if function_in_pohidna * (-x_in_zero) < 0:
        string += "- " + str(round((default_funct + function_in_pohidna * (-x_in_zero)), 2))[1:]
    else:
        string += "+ " + str(round((default_funct + function_in_pohidna * (-x_in_zero)), 2))
    return string

def get_root(function, param_a, param_b):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    num = None
    if isinstance(function, str):
        function = eval('lambda x: ' + function)
    for i in range(param_a * 1000, param_b * 1000):
        if function(i / 1000) == 0:
            num = round((i / 1000), 2)
    return num

import doctest
doctest.testmod()
    # return round(((function(param_a) + function(param_b)) / 2), 2)

#print(get_root('x', -1, 1))

print(get_root(lambda x: x + 6, -1, 1))