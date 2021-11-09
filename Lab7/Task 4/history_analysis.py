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
    try:
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
        try:
            for i in range(number):
                return_set.add(list_of_counted[i][1])
        except IndexError:
            return return_set
        return return_set
    except IndexError:
        return set()

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
    >>> get_url_info([('google.com', 'GOOGLE', "2021-11-08", '13:45:10.10', 2020)], "google.com")
    ('GOOGLE', '2021-11-08', '13:45:10.10', 1, 2020.0)
    """
    list_required = []
    for elem in visits:
        if elem[0] == url:
            list_required.append(elem)

    common_list = []
    duration = 0
    for date in list_required:
        dates = date[2]
        times = date[3]
        duration += int(date[4])
        common_list.append((dates, times))
    if len(list_required) == 0:
        return "", "", "", 0, 0
    duration = duration/len(list_required)
    tupple_max = max(common_list)

    return (list_required[0][1], tupple_max[0], tupple_max[1], len(list_required), duration)

#print(get_url_info([('url','topic','1992-02-11','01:05:36.66',97865), ('url','topic','2021-11-28','12:05:36.66',9876), ('url','topic','2021-11-07','12:05:36.66',878654), ('url','topic','2021-11-07','12:05:36.66',3456), ('url1','topic','2021-11-07','12:05:36.66',865), ('url1','topic','2021-11-07','12:05:36.66',34567), ('url1','topic','2021-11-07','12:05:36.66',97675), ('url1','topic','2021-11-07','12:05:36.66',3425), ('url1','topic','2021-11-07','12:05:36.66',76566), ('url1','topic','2021-11-07','12:05:36.66',6543), ('w','topic','2021-11-07','12:05:36.66',7643), ('url2','topic','2021-11-07','12:05:36.66',560)], 'url'))
print(get_url_info([('url','topic','2022-2-11','11:05:36.66',97865), ('url','topic','2022-2-11','12:15:36.66',9876)], 'url'))
print(most_frequent_sites([('url','topic','2022-2-11','11:05:36.66',97865)], 5))
import doctest
doctest.testmod()
