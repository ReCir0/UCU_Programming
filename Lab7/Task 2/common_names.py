'''Lab 7.2'''
def common_names(female_names, male_names):
    '''
    Checks simular names of boys and girls
    returns the simular names
    >>> common_names(names_read('male.txt'), \
names_read('female.txt'))  #doctest: +ELLIPSIS
    {...
    '''
    vovels = ["a", "e", 'i', "o", "u"]
    all_set = []
    for male in male_names:
        if male in female_names and male[0].lower() in vovels:
            all_set.append(male)

    return set(all_set)

def names_read(file_name):
    '''
    Reads a file and returns a list of names
    >>> names_read('male.txt') #doctest: +ELLIPSIS
    {...
    '''
    set_of_names = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line.strip()
            line = line[:-1]
            set_of_names.append(line)
    return set(set_of_names)
