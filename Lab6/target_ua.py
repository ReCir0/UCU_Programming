'''
Ukrainian target game
'''
from random import choice

def generate_grid():
    '''
    Generates a random grid
    '''
    alp = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з',\
    'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',\
    'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    letters = []
    while len(letters) < 5:
        letter = choice(alp)
        if letter not in letters:
            letters.append(letter)
    return letters

def get_words(url, letters):
    '''
    Checks words
    >>> get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']) #doctest: +ELLIPSIS
    [('габа', 'noun'), ('габро', 'noun'), ('гавин', 'adjective')...
    '''
    list_cort = []
    with open(url) as file:
        for line in file:
            line.strip()
            line.encode('utf-8')
            len_line = len(line)
            for i in range(len_line):
                if line[i] == " ":
                    word, symbols = line[0:i], line[i:]
                    break
            symbols = symbols.lstrip()
            if len(word) > 5 or len(word) < 1:
                continue
            for i in letters:
                if i == word[0]:
                    break
            else:
                continue
            if "noninfl" in symbols or "intj" in symbols:
                continue
            if symbols.startswith("adv") or symbols.startswith("/adv"):
                list_cort.append((word, "adverb"))
                continue
            if symbols.startswith("adj") or symbols.startswith("/adj"):
                list_cort.append((word, "adjective"))
                continue
            if "/n" in symbols or "noun" in symbols:
                list_cort.append((word, "noun"))
                continue
            if "/v" in symbols:
                list_cort.append((word, "verb"))
                continue
    return list_cort

def check_user_words(user_words, part_of_len, letters, dict_of_words):
    """
    Checks which of the user words meet the requirements and returns a list
    of words guessed
    >>> check_user_words(['гаяти', 'гнати', 'ініціалізація', 'узяти', 'щавель'], "verb",\
['ю', 'щ', 'я', 'ц', 'г'], get_words("base.lst", ['ю', 'щ', 'я', 'ц', 'г']))
    (['гаяти', 'гнати'], ['гнити', 'гнути', 'гоїти', 'грати', 'гріти', 'густи', \
'юшити', 'явити', 'яріти', 'ячати'])
    """
    correct_words = []
    missed_words = []
    for i in range(len(user_words) - 1):
        try:
            if user_words[i][0] not in letters or len(user_words[i]) > 5:
                del user_words[i]
        except IndexError:
            break

    for i in dict_of_words:
        if i[0] in user_words:
            if i[1] == part_of_len:
                correct_words.append(i[0])
        elif i[0] not in user_words:
            if i[1] == part_of_len:
                missed_words.append(i[0])
    return correct_words, missed_words


def get_user_words():
    """
    Gets with input user words
    """
    return input("Введіль ваші слова:").lower().split()

def language_part_gen():
    """
    Generates a random language part
    """
    parts_of_lan = ['noun', 'verb', 'adjective', 'adverb']
    return choice(parts_of_lan)

def results():
    """
    The main function that calls all other functions
    """
    words = generate_grid()
    len_words = len(words)
    for i in range(len_words):
        words[i] = words[i].lower()
    print(words)
    part_of_len = language_part_gen()
    good_words = get_words("base.lst", words)
    user_words = get_user_words()
    correct_words, missed_words = check_user_words\
    (user_words, part_of_len, words, good_words)

    print("Частина мови:", part_of_len)
    print("Ви вгадали:", len(correct_words), " слів правильно")
    print("Ви пропустили ці слова:", *missed_words)
