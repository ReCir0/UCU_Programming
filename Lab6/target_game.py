''' A game of guessing words '''
from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters = []
    sub_grid = []
    for i in range(3):
        for j in range(3):
            sub_grid.append(chr(random.randrange(65, 90 + j - j + i - i)))
        letters.append(sub_grid)
        sub_grid = []
    return letters


def get_words(file: str, text: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('en.txt', [el for el in 'wumrovkif'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', \
'kori', 'miro', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    """
    alph = []
    for i in range(26):
        alph.append(chr(97 + i))
    for i in range(9):
        if text[i] in alph:
            try:
                alph.remove(text[i])
            except ValueError:
                continue
    try:
        with open(file) as file:
            counter = 0
            words = []
            for line in file:
                breaking = False
                line = line.lower()
                line = line[:-1]
                if len(line) < 4 or counter < 3:
                    counter += 1
                    continue
                if text[4] in line:
                    for i in range(len(alph)):
                        if alph[i] in line:
                            breaking = True
                            break
                        for j in range(9):
                            if text.count(text[j]) < line.count(text[j]):
                                breaking = True
                                break
                else:
                    breaking = True
                if breaking:
                    continue
                words.append(line)
                counter += 1
    except FileNotFoundError:
        return None
    return words

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    words = input().lower().split()
    return words


def get_pure_user_words(user_words: List[str], letters: List[str],\
    correct_words: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    user_words_fake = []
    for i in user_words:
        if i in correct_words:
            continue
        user_words_fake.append(i)

    alph = []
    for i in range(26):
        alph.append(chr(97 + i))
    for i in range(9):
        if letters[i] in alph:
            try:
                alph.remove(letters[i])
            except ValueError:
                continue
    words = []
    for line in user_words_fake:
        breaking = False
        line = line.lower()
        if len(line) < 4:
            continue
        if letters[4] in line:
            for i in range(len(alph)):
                if alph[i] in line:
                    breaking = True
                    break
                for j in range(9):
                    if letters.count(letters[j]) < line.count(letters[j]):
                        breaking = True
                        break
        else:
            breaking = True
        if breaking:
            continue
        words.append(line)
    return words

def results():
    '''
    Starts the game
    '''
    letters = generate_grid()
    text = ""
    for i in range(3):
        for j in range(3):
            text += letters[i][j].lower()

    print(letters)
    user_words = get_user_words()
    correct_words = get_words("en.txt", text)
    fake_words = get_pure_user_words(user_words, text, correct_words)

    not_entered = correct_words
    for i in user_words:
        if i in correct_words:
            not_entered.remove(i)
    correct_words_user = len(correct_words) - len(not_entered)

    print(correct_words)
    print(user_words)
    print(not_entered)

    with open("result.txt", "w") as result:
        result.write(str(correct_words_user))
        result.write("\n")
        result.write(str(not_entered))
        result.write("\n")
        result.write(str(user_words))
        result.write("\n")
        result.write(str(fake_words))
        result.write("\n")
        result.close()
        
l
