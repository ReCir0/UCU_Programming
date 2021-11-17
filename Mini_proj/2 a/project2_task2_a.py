'''Mini proj tasl 2 a'''
import argparse
import os

def list_files(startpath):
    '''
    Returns either the path was correct to a file or not
    '''
    for folders, _, file_names in os.walk(startpath):
        directory_level = folders.replace(startpath, "")
        directory_level = directory_level.count(os.sep)
        spacing_in_dir = "│  "
        print(spacing_in_dir * directory_level, "├───── ", os.path.basename(folders), "/", sep = "")
        check_if_empty = 1
        len_file_names = len(file_names)
        for i in range(len_file_names):
            if i == len(file_names) - 1:
                print(spacing_in_dir * (directory_level + 1), "└───── ", file_names[i], sep = "")
                continue
            print(spacing_in_dir * (directory_level + 1), "├───── ", file_names[i], sep = "")
    try:
        return check_if_empty
    except UnboundLocalError:
        return 0

def read_info():
    '''
    Reads arguments from console
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('start_directory', \
    help = 'The path to the folder where tree starts')
    arguments = parser.parse_args()
    return arguments.start_directory

# If statement checks if the path was correct
if list_files(read_info()) == 0:
    print("The path was incorrect")
