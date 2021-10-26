from typing import List
import urllib.request

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url
    
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    list_web = []
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            if line[0].isdigit():
                line = line.split('\t')
                list_web.append(line)
            
            
    #         list_web.append(line)
    # list_web.pop(0)   
    # list_web.pop(0)
    # for i in range(200):
            
    return list_web


        

def write_csv_file(url: str):
    file = open("total.csv", "w")
    file.write("fdsjifodsj\n")
    
    

print(read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1))
