'''Lab 9.1'''
def find_film_keywords(film_keywords: dict, film_name: str):
    '''
    Finds keywords in a particular film
    >>> find_film_keywords({'Iron': ['Avengers: Endgame', 'What If', \
"One", 'A cave'], 'World': ['One', 'What If', "Two"]}, 'What If') #doctest: +ELLIPSIS
    {...
    '''
    result = []
    for key in film_keywords:
        value = film_keywords[key]
        for film in value:
            if film == film_name:
                result.append(key)
    return set(result)

def find_films_with_keywords(film_keywords: dict, num_of_films: int):
    '''
    Returns films with most keywords
    >>> find_films_with_keywords({'Iron': ['Avengers: Endgame', 'What If', \
"One", 'A cave'], 'World': ['One', 'What If', "Two"]}, 6)
    [('One', 2), ('What If', 2), ('Two', 1), ('A cave', 1), ('Avengers: Endgame', 1)]
    '''
    dict_2 = {}
    mass_fin = []
    for key in film_keywords:
        value = film_keywords[key]
        for film in value:
            if film in dict_2:
                dict_2[film].append(key)
            else:
                dict_2[film] = [key]
    for key in dict_2:
        mass_fin.append((key, len(dict_2[key])))
    mass_fin = sorted(mass_fin, key=lambda amount: amount[1])
    mass_fin.reverse()

    return mass_fin[:num_of_films]

import doctest
doctest.testmod()

dict = {'Iron': ['Avengers: Endgame', 'What If', "One", 'A cave'], 'World': ['One', 'What If', "Two"]}
print(find_films_with_keywords(dict, 6))
