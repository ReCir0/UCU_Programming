'''quadrangle_area'''
def four_lines_area(koef_1, num_1, koef_2, num_2, koef_3, num_3, koef_4, num_4):
    '''
    The main function that calculates everything
    and starts all the functions in a correct order
    '''
    koef_mas = [koef_1, koef_2, koef_3, koef_4]
    bes_mas = [num_1, num_2, num_3, num_4]
    x_coord_1, y_coord_1 = lines_intersection(koef_mas[0], bes_mas[0], koef_mas[1], bes_mas[1])
    x_coord_2, y_coord_2 = lines_intersection(koef_mas[1], bes_mas[1], koef_mas[2], bes_mas[2])
    x_coord_3, y_coord_3 = lines_intersection(koef_mas[2], bes_mas[2], koef_mas[3], bes_mas[3])
    x_coord_4, y_coord_4 = lines_intersection(koef_mas[3], bes_mas[3], koef_mas[0], bes_mas[0])
    side1 = distance(x_coord_1, y_coord_1, x_coord_2, y_coord_2)
    side2 = distance(x_coord_2, y_coord_2, x_coord_3, y_coord_3)
    side3 = distance(x_coord_3, y_coord_3, x_coord_4, y_coord_4)
    side4 = distance(x_coord_4, y_coord_4, x_coord_1, y_coord_1)
    diagonal1 = distance(x_coord_1, y_coord_1, x_coord_3, y_coord_3)
    diagonal2 = distance(x_coord_2, y_coord_2, x_coord_4, y_coord_4)
    area = quadrangle_area(side1, side2, side3, side4, diagonal1, diagonal2)
    return area

def lines_intersection(koef_1, num_1, koef_2, num_2):
    '''
    Function calculates the coordinates of the intersections
    '''
    if koef_1 == koef_2:
        return
    x_coord = (num_2 - num_1)/ (koef_1 - koef_2)
    y_coord = koef_1 * x_coord + num_1
    # Точка перетину
    return round(x_coord, 2), round(y_coord, 2)

def distance(x_coord_1, y_coord_1, x_coord_2, y_coord_2):
    '''
    Calculates distance between two dots
    '''
    distance_between = ((x_coord_1 - x_coord_2) ** 2 + (y_coord_1 - y_coord_2) ** 2) ** 0.5
    return round(distance_between, 2)

def quadrangle_area(side1, side2, side3, side4, diagonal1, diagonal2):
    '''
    Function calculates the area of an quadrangle
    '''
    area = ((4 * (diagonal1 ** 2) * (diagonal2 ** 2) - (side2 ** 2 + side4 ** 2 - \
    side1 ** 2 - side3 ** 2) ** 2) / 16) ** 0.5
    try:
        return round(area, 2)
    except TypeError:
        return

print(four_lines_area(0, 20, 3, -0.3, 0.1, 10, -5, 3))
