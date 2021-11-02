import random
def generate_grid():
    '''
    Generates a random grid
    '''
    alp = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    letters = []
    while len(letters) < 5:
        letter = random.choice(alp)
        if letter not in letters:
            letters.append(letter)
    return letters

print(generate_grid())



# letter = random.choice(choices)
#     if letter not in grid:
#         grid.append(letter)
