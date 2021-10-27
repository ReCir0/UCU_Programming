'''Pascal triangle generation'''
def generate_pascal_triangle(num):
    '''
    Generates pascal triangle
    >>> print(generate_pascal_triangle(5))
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    '''
    triangle = []
    for i in range(num):
        triangle_sub = []
        for j in range(i + 1):
            if i < 2:
                triangle_sub.append(1)
                continue
            if j == 0:
                triangle_sub.append(1)
                continue
            if j == i:
                triangle_sub.append(1)
                continue
            triangle_sub.append(triangle[i-1][j] + triangle[i-1][j - 1])
        triangle.append(triangle_sub)
    return triangle
