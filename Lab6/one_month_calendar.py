'''Lab 6.8'''
import datetime
import math

def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]

    >>> weekday_name(3)
    'thu'
    """
    days_mass = [("mon", 0), ("tue", 1),("wed", 2), \
    ("thu", 3), ("fri", 4), ("sat", 5), ("sun", 6)]
    len_days = len(days_mass)
    for i in range(len_days):
        if days_mass[i][1] == number:
            return days_mass[i][0]

def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    try:
        date_mass = date.split(".")
        date = int(date_mass[0])
        month = int(date_mass[1])
        year  = int(date_mass[2])
        if year <= 1583:
            raise AssertionError('the date is invalid')
        week_num = datetime.date(year, month, date).weekday()
        return week_num
    except:
        raise AssertionError('the date is invalid')

def calendar(month: int, year: int) -> str:
    """Return a string representing a\
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    calendar_full = "mon tue wed thu fri sat sun\n"
    date = "01." + str(month).zfill(2) + "." + str(year)
    start_day = weekday(date)
    big_months = [1, 3, 5, 7, 8, 10, 12]
    if month == 2:
        amount_of_days = 28
        if year % 4 == 0:
            amount_of_days = 29
    elif month in big_months:
        amount_of_days = 31
    else:
        amount_of_days = 30
    amount_of_weeks = math.ceil((start_day + amount_of_days) / 7)
    day_number = 1
    for j in range(amount_of_weeks):
        for i in range(7):
            if day_number == amount_of_days:
                calendar_full += " " + str(day_number)
                break
            if i < start_day and j == 0:
                spaces = "    "
                calendar_full += spaces
            elif day_number < 10:
                if i == 6:
                    calendar_full += "  " + str(day_number)
                    day_number += 1
                    break
                calendar_full += "  " + str(day_number) + ' '
                day_number += 1
            elif i == 6:
                calendar_full += " " + str(day_number)
                day_number += 1
            else:
                calendar_full += " " + str(day_number) + ' '
                day_number += 1
        if j == amount_of_weeks - 1:
            break
        calendar_full += "\n"

    return calendar_full

calendar(12 , 2015)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
