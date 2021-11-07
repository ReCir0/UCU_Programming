def dict_reader_tuple(file_url):
    '''
    Reads a file and returns its elements
    '''
    dictianry = {}
    elem = 1
    with open(file_url, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            word = line[:line.find(' ')]
            line = line[line.find(' ') + 1:]
            index = line[:line.find(' ')]
            line = line[line.find(' ') + 1:]
            pronanciation = line.split(" ")
            dictianry[elem] = (word, int(index), pronanciation)
            elem += 1
    return dictianry
            
print(dict_reader_tuple("cmudict.txt"))