'''1.b'''
import argparse
def string_change():
    '''
    Calls the function get_args to get data from a user
    and either changes string in file or prints it in console
    '''
    change_from_str, change_to_str, url, inplace = get_args()
    print(change_from_str, change_to_str, url, inplace)
    to_write = ""
    with open(url, "r", encoding = "utf-8") as file:
        for line in file:
            #while line.find(change_from_str) != -1:
            line = line.replace(change_from_str, change_to_str)
            if inplace:
                to_write += line
            else:
                print(line, end = "")
    if inplace:
        with open(url, 'w', encoding = "utf-8") as file:
            file.write(to_write)
    else:
        print()

def get_args():
    '''
    With the help of argparse gets argumemts from a user
    and returns them
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("change_from_string", help = 'First argument')
    parser.add_argument("change_to_string", help = 'Second argument')
    parser.add_argument("file_url", help = "File url")
    parser.add_argument("--inplace",  action='store_true')
    arguments = parser.parse_args()
    return arguments.change_from_string, arguments.change_to_string, \
    arguments.file_url, arguments.inplace

string_change()

#python3 first_b.py hello 11111 substrings.txt --inplace