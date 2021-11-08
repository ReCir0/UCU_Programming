'''Lab 7.3'''
def dict_reader_tuple(file_url):
    '''
    Reads a file and returns its elements
    >>> dict_reader_tuple("cmudict.txt") #doctest: +ELLIPSIS
    [('A', 1, ['AH0']),...
    '''
    dictianry = []
    with open(file_url, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            word = line[:line.find(' ')]
            line = line[line.find(' ') + 1:]
            index = line[:line.find(' ')]
            line = line[line.find(' ') + 1:]
            pronanciation = line.split(" ")
            dictianry.append((word, int(index), pronanciation))
    return dictianry

def dict_reader_dict(file_dict):
    '''
    Returns a dictinary of words and pronanciation
    >>> dict_reader_dict("cmudict.txt") #doctest: +ELLIPSIS
    {'A': {...
    '''
    dictianry = {}
    with open(file_dict, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            word = line[:line.find(' ')]
            line = line[line.find(' ') + 1:]
            line = line[line.find(' ') + 1:]
            pronanciation = tuple(line.split(" "))
            if word in dictianry:
                value = dictianry[word]
                value.add(pronanciation)
                dictianry[word] = value
            else:
                words = set()
                words.add(pronanciation)
                dictianry.setdefault(word, words)
        return dictianry

def dict_invert(dct):
    '''
    Inverts the dict
    >>> dict_invert({'WATER':{('W', 'A', 'T', 'E', 'R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    '''
    if isinstance(dct, dict):
        pass
    else:
        dic_val = dct
        dct = {}
        for element in dic_val:
            if element[0] in dct.keys():
                pron = tuple(element[2])
                dct[element[0]].add(pron)
            else:
                pron = set()
                pron.add(tuple(element[2]))
                dct[element[0]] = pron
    dictianry = {}
    for word in dct:
        pronanciation = dct[word]
        keyyy = len(pronanciation)
        pronanciation = list(pronanciation)
        if keyyy in dictianry:
            dic_val = []
            for i in range(keyyy):
                val_of_key = tuple((word, pronanciation[i]))
                dic_val.append(val_of_key)
            dic_val = set(dic_val)
            dictianry[keyyy].update(dic_val)
        else:
            set_app = set()
            for i in range(keyyy):
                val_of_key = tuple((word, pronanciation[i]))
                set_app.add(val_of_key)
            dictianry.setdefault(keyyy, set_app)
    dictinarry = {}
    for i in sorted(dictianry.keys()):
        dictinarry[i] = dictianry[i]
    return dictinarry
