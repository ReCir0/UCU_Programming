
def semester_calendar(output_type, year, first_month, last_month):
    import calendar
    """
    >>>  semester_calendar("txt", 2021, 10, 10)
        October 2021
    Mo Tu We Th Fr Sa Su

                1  2  3

    4  5  6  7  8  9 10

    11 12 13 14 15 16 17

    18 19 20 21 22 23 24

    25 26 27 28 29 30 31

    """
    calendar = ""
    if output_type == "html" or output_type == "txt":
        pass
    else:
        return None
    if output_type == "html":
        for i in range(last_month - first_month + 1):
            cal_html = calendar.HTMLCalendar(0)
            calendar += cal_html.formatmonth(year, first_month + i)
    elif output_type == "txt":
        for i in range(last_month - first_month + 1):
            for i in range((last_month - first_month) + 1):
                calendar += calendar.month(year, first_month + i)
                first_month = first_month + 1
    return calendar

print(semester_calendar("txt", 2021, 10, 12))