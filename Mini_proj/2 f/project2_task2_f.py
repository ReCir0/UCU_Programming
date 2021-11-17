'''Mini-proj 2_b'''
import argparse
import os
import re

def find_a_file():
    '''
    Finds a file by string
    '''
    to_find_string, file_search, show_lines, only_show_counts = read_info()
    elements = []
    is_star = False
    start_directory = os.getcwd()
    # If * was entered, checks the ending of files
    # Walking through directory and checks for files
    for folders, _, file_names in os.walk("../"):
        len_file_names = len(file_names)
        for i in range(len_file_names):
            if re.search(file_search, file_names[i]):
                os.chdir(folders)
                with open(file_names[i]) as file:
                    elements.append((file_names[i], file.readlines()))
                os.chdir(start_directory)
    result = []
    for file in elements:
        strings = []
        index = []
        for i in range(len(file[1])):
            if re.search(to_find_string, file[1][i]):
                strings.append(file[1][i])
                index.append(i + 1)
        if strings != []:
            result.append((file[0], strings, index))
    # If directory[] is empty -- no files were found
    if elements:
        pass
    else:
        print("No files were found :(")
        return
    if only_show_counts:
        print(len(result))
        return
    if result:
        text = ""
        for i in range(len(result)):
            text += result[i][0] + "\n"
            if show_lines:
                for j in range(len(result[i][1])):
                    text += str(result[i][2][j]) + ": " + result[i][1][j]
            else:
                for line in result[i][1]:
                    text += line
            text += "\n\n\n"
        print(text, end = "")
    else:
        print("No matches were found :(")

def read_info():
    '''
    Reads and returns arguments from console
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('to_find_string', type = str,\
    help = 'String that you need to find in files')
    parser.add_argument('file_search', type = str, \
    help = 'Files that you need to search in')
    parser.add_argument('--show_lines', action = 'store_true', \
    help = 'Print lines as "number:line"')
    parser.add_argument('--only_show_counts', action = 'store_true', \
    help = 'Print only the amount of matches')
    arguments = parser.parse_args()
    return arguments.to_find_string, arguments.file_search, \
    arguments.show_lines, arguments.only_show_counts

find_a_file()
