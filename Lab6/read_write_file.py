'''Program that analyses the list of students'''
from typing import List
import urllib.request

def read_input_file(url: str, number = 77) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. \
В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    list_web = []
    element = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            if line[0].isdigit():
                line = line.split('\t')
                element.append(line[0])
                element.append(line[1])
                if line[2] == 'До наказу':
                    element.append("+")
                    element.append(line[3])
                    continue
                element.append("-")
                element.append(line[3])
                continue
            if line.find('документа') != -1:
                line = line.split(' ')
                element.append(line[5])
                list_web.append(element)
                element = []
    return_list = []
    for i in range(number):
        return_list.append(list_web[i])
    return return_list

def write_csv_file(url: str):
    '''
    Creates a csv file
    >>> write_csv_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt')
    '''
    file = open("total.csv", "w")
    mass = read_input_file(url)
    text = ""
    for i in range(77):
        for j in range(len(mass[i])):
            if j == len(mass[i]) - 1:
                text += mass[i][j]
                continue
            text += mass[i][j] + ","
        text += "\n"
    file.write("№,ПІБ,Д,Заг.бал,С.б.док.осв.\n")
    file.write(text)
    file.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod()