'''Lab 5'''
def total_occurrences(string_1, string_2, search):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that search occurs in string_1 and string_2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    return (string_1 + string_2).count(search)

def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that search occurs in string_1 and string_2.
    >>> tdyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
    дивоит кота по хвилях катав - дивокит у воді, кіт на дивокиті
    >>> tdyvo_insert("На морі купались кити та лежали на сонці", "ки")
    на морі купались дивокити та лежали на сонці
    >>> tdyvo_insert("кит", "ки")
    дивокит
    """
    i = 0
    sentence.lower()
    while i < (len(sentence)):
        if sentence[0] == "к" or sentence[0] == "К":
            sentence = sentence[:i] + "диво" + sentence[i:]
            i += 5
            continue
        if sentence[i] == " ":
            if sentence[i + 1] == flag[0]:
                if sentence[i + 2] == flag[1]:
                    sentence = sentence[:i + 1] + "диво" + sentence[i + 1:]
        i += 1
    return sentence.lower()

import calendar
def semester_calendar(output_type, year, first_month, last_month):
    '''
    Making a calendar
    '''
    try:
        years = ""
        if output_type == "txt":
            for i in range(last_month - first_month + 1):
                years += (calendar.month(year, first_month + i))
        if output_type == "html":
            for i in range(last_month - first_month + 1):
                cal_html = calendar.HTMLCalendar(calendar.MONDAY)
                years += cal_html.formatmonth(year, first_month + i)
        return years
    except TypeError:
        return None

print(help(print))