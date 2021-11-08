'''Lab 7.4'''
def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> sites_on_date([('google.com', 'GOOGLE', "2021-11-08", '13:45:10:10', '2020')], "2021-11-08")
    {'google.com'}
    """
    all_sites_visited = set()
    for site_info in visits:
        if site_info[2] == date:
            all_sites_visited.add(site_info[0])
    if len(all_sites_visited) >= 1:
        return all_sites_visited

def most_frequent_sites(visits, number):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> most_frequent_sites([('google.com', 'GOOGLE', "2021-11-08", '13:45:10:10', '2020')], 1)
    {'google.com'}
    """
    list_of_visits = []
    for name in visits:
        list_of_visits.append(name[0])
    set_of_lists = list(set(list_of_visits))
    list_of_counted = []
    for name in set_of_lists:
        list_of_counted.append((list_of_visits.count(name), name))
    list_of_counted.sort()
    list_of_counted.reverse()
    return_set = set()
    for i in range(number):
        return_set.add(list_of_counted[i][1])
    if len(return_set) >= 1:
        return return_set

def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    >>> get_url_info([('google.com', 'GOOGLE', "2021-11-08", '13:45:10:10', '2020')], "google.com")
    ['GOOGLE', '2021-11-08', '13:45:10:10', 1, 2020]
    """
    list_required = []
    for elem in visits:
        if elem[0] == url:
            list_required.append(elem)

    date_list = []
    time_list = []
    duration = 0
    for date in list_required:
        dates = date[2]
        times = date[3]
        duration += int(date[4])
        dates = dates[:4] + dates[5:7] + dates[8:]
        times = times[:2] + times[3:5] + times[6:8] + times[9:]
        date_list.append(dates)
        time_list.append(times)
    duration = int(duration/len(list_required))
    date_max = max(date_list)
    time_max = max(time_list)
    date_max = date_max[:4] + '-' + date_max[4:6] + '-' + date_max[6:]
    time_max = time_max[:2] + ':' + time_max[2:4] + ':' + \
    time_max[4:6] + ':' + time_max[6:8]

    return [list_required[0][1], date_max, time_max, len(list_required), duration]
