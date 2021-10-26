from typing import List, Tuple, Callable, Union
    
def title_length(tupple_mas: Tuple[str]) -> int:
    '''
    >>> title_length([('a', 1.12), ('b', 2.21), ('c', 4.11)])
    2
    '''
    return len(tupple_mas[0])

def last_word(tupple_mas: Tuple[str]) -> str:
    '''
    >>> print('Hello')
    Hello
    '''
    return tupple_mas[0].split(" ")[-1]

def song_length(tupple_mas: Tuple[str]) -> float:
    '''
    >>> song_length([('a', 1.12), ('b', 2.21), ('c', 4.11)])
    ('b', 2.21)
    '''
    return tupple_mas[1]

def sort_songs(song_titles: List[str], length_songs: List[str], key: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    '''
    >>> sort_songs(['a', 'b', 'c'], [1.12, 2.21, 4.11], song_length)
    [('a', 1.12), ('b', 2.21), ('c', 4.11)]
    '''
    if len(song_titles) != len(length_songs):
        return
    else:
        tupple_mas = []
        for i in range(len(song_titles)):
            tupple_mas.append((song_titles[i], length_songs[i]))
    return sorted(tupple_mas, key = key)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

sort_songs(['a', 'b', 'c'], [1.12, 2.21, 4.11], song_length)
