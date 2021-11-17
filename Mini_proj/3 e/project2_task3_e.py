"Mini-proj 3_e"
import argparse
import os
import zipfile

def connect():
    '''
    The function that connects zip files
    '''
    first_zip, second_zip, new_zip_name = read_info()
    if new_zip_name.endswith(".zip") is False:
        print("The path to zip that will be created isn't a zip")
        return
    new_zip = zipfile.ZipFile(new_zip_name, 'w')
    try:
        first_zip_file = zipfile.ZipFile(first_zip, 'r')
        first_zip_file.extractall()
    except FileNotFoundError:
        if first_zip.endswith(".zip"):
            print("The path to the first zip is wrong")
        else:
            print("The path to the first zip you entered isn't a zip file")
        return
    except IsADirectoryError:
        print("The path to the first zip is a directory")
        return
    try:
        second_zip_file = zipfile.ZipFile(second_zip, 'r')
        second_zip_file.extractall()
    except FileNotFoundError:
        if second_zip.endswith(".zip"):
            print("The path to the first zip is wrong")
        else:
            print("The path to the first zip you entered isn't a zip file")
        return
    except IsADirectoryError:
        print("The path to the first zip is a directory")
        return
    os.chdir(first_zip[:-4])
    for file in os.listdir():
        new_zip.write(os.path.join(file))
    os.chdir("../")
    os.chdir(second_zip[:-4])
    for file in os.listdir():
        new_zip.write(os.path.join(file))
    new_zip.close()
    os.chdir("../")
    list_first = [first_zip, second_zip, new_zip_name, __file__]
    list_to_delete = set(os.listdir('.')) ^ set(list_first)
    for del_file in list_to_delete:
        try:
            delete_file(del_file)
        except NotADirectoryError:
            os.remove(del_file)

def delete_file(path):
    '''
    Deletes a folder full of files and folders
    '''
    for directory, folders, files in os.walk(path, topdown = False):
        [os.remove(os.path.join(directory, file)) for file in files]
        [os.rmdir(os.path.join(directory, folder)) for folder in folders]
    if os.path.exists(path):
        os.rmdir(path)

def read_info():
    '''
    Reads and returns arguments from console
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('first_zip', \
    help = 'The path to first zip file')
    parser.add_argument('second_zip', \
    help = 'The path to second zip file')
    parser.add_argument('new_zip', \
    help = 'The path to zip where all information will be')
    arguments = parser.parse_args()
    return arguments.first_zip, arguments.second_zip, arguments.new_zip

connect()
