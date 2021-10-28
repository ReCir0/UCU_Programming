from typing import List
import random

def board_generation() -> List[list]:
    """
    Generates a game board of 16 x 4 size, i.e. two dimensional list (array) of 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    list_of_posibilities = [0, "g", "w"]
    board_mas = []
    for i in range(16):
        sub_board_mas = []
        check = True
        for j in range(4):
            if 0 in sub_board_mas and check:
                list_of_posibilities.remove("g")
                list_of_posibilities.remove("w")
                check = False
            sub_board_mas.append(random.choice(list_of_posibilities))
        sub_board_mas.reverse()
        board_mas.append(sub_board_mas)
        list_of_posibilities = [0, "g", "w"]
        
    return board_mas

def winning_combination(board: List[list]) -> bool:
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions if there is winning combination or False if not.

    >>> winning_combination([[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], ['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'g', 'g', 'w'], [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], ['w', 'g', 'g', 'g'], ['w', 'w', 'g', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 'g', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'g'], [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([[0, 'w', 'w', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'w', 'g'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 'g', 'w', 'g'], ['g', 'g', 'w', 'g'], ['w', 'g', 'w', 'g']])
    (True, [[(2, 13), (2, 14), (2, 15), (2, 0)], [(3, 5), (3, 6), (3, 7), (3, 8)]
    >>> winning_combination([[0, 0, 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'g', 'g'], ['w', 'w', 'g', 'g'], ['w', 'g', 'g', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination([[0, 0, 'w', 'w'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 'w', 'g', 'g'], ['g', 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 'w', 'w', 'w'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w']])
    (True, [[(3, 4), (3, 5), (3, 6), (3, 7)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15), (3, 0), (3, 1)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    
    """
    wining_combinations = []
    # # Checking vertical combinations
    # for i in range(len(board)):
    #     wining_comb = []
    #     for j in range(4):
    #         if board[i][0] == board[i][j] and board[i][j] != 0:
    #             wining_comb.append((j, i))
    #     if len(wining_comb) == 4:
    #         wining_combinations.append(wining_comb)
    # wining_comb = []
    # # Checking horizontal combinations
    # for i in range(len(board)):
    #     for j in range(4):
    #         if board[i - 3][j] == board[i][j] and board[i - 2][j] == board[i][j] \
    #             and board[i - 1][j] == board[i][j] and board[i][j] != 0:
    #             for x in range(4):
    #                 wining_comb.append((j, i - 3 + x))
    #             wining_combinations.append(wining_comb)
    #     wining_comb = []
    # # Checking diagonal combinations
    # for i in range(len(board)):
    #     if board[i - 3][0] == board[i - 2][1] and board[i][0] == board[i - 1][2] \
    #         and board[i][0] == board[i][3] and board[i - 3][0] != 0:
    #         for x in range(4):
    #             wining_comb.append((x, i - 3 + x))
    #         wining_combinations.append(wining_comb)
            
            
    # Checking vertical combinations
    for i in range(len(board)):
        wining_comb = []
        for j in range(4):
            if board[i][0] == board[i][j] and board[i][j] != 0:
                wining_comb.append((j, i))
        if len(wining_comb) == 4:
            wining_combinations.append(wining_comb)
    wining_comb = []
    # Checking horizontal combinations
    for i in range(len(board) - 3):
        for j in range(4):
            if board[i][j] == board[i + 1][j] and board[i][j] == board[i + 2][j] \
                and board[i][j] == board[i + 3][j] and board[i][j] != 0:
                for x in range(4):
                    wining_comb.append((j, i + x))
                wining_combinations.append(wining_comb)
                wining_comb = []
    for j in range(4):
        if (board[13][j] == board[14][j] and board[13][j] == board[15][j] \
            and board[13][j] == board[0][j] and board[13][j] != 0):
            for x in range(3):
                wining_comb.append((j, 13 + x))
            wining_comb.append((j, 0))
            wining_combinations.append(wining_comb)
            wining_comb = []
        if (board[14][j] == board[15][j] and board[14][j] == board[0][j] \
            and board[14][j] == board[1][j] and board[14][j] != 0):
            for x in range(2):
                wining_comb.append((j, 14 + x))
            wining_comb.append((j, 0))
            wining_comb.append((j, 1))
            wining_combinations.append(wining_comb)
            wining_comb = []
        if (board[15][j] == board[0][j] and board[15][j] == board[1][j] \
            and board[15][j] == board[2][j] and board[15][j] != 0):
            wining_comb.append((j, 15))
            for x in range(3):
                wining_comb.append((j, x))
            wining_combinations.append(wining_comb)
            wining_comb = []
    wining_combinations.sort()
    
    # Checking diagonal combinations
    for i in range(len(board) - 3):
        if board[i][0] == board[i + 1][1] and board[i][0] == board[i + 2][2] \
            and board[i][0] == board[i + 3][3] and board[i][0] != 0:
            for x in range(4):
                wining_comb.append((x, i + x))
            wining_combinations.append(wining_comb)
            wining_comb = []
        
    if (board[13][0] == board[14][1] and board[13][0] == board[15][2] \
        and board[13][j] == board[3][j] and board[13][0] != 0):
        for x in range(3):
            wining_comb.append((x, 13 + x))
        wining_comb.append((3, 0))
        wining_combinations.append(wining_comb)
        wining_comb = []
    if (board[14][0] == board[15][1] and board[14][0] == board[0][2] \
        and board[14][0] == board[1][3] and board[14][0] != 0):
        for x in range(2):
            wining_comb.append((x, 14 + x))
        wining_comb.append((j, 0))
        wining_comb.append((j, 1))
        wining_combinations.append(wining_comb)
        wining_comb = []
    if (board[15][0] == board[0][1] and board[15][0] == board[1][2] \
        and board[15][0] == board[2][3] and board[15][0] != 0):
        wining_comb.append((0, 15))
        for x in range(3):
            wining_comb.append((x + 1, x))
        wining_combinations.append(wining_comb)
        wining_comb = []
    wining_combinations.sort()


    # Cortage with TRUE/FALSE
    if len(wining_combinations) != 0:
        is_wining = True
    else:
        return False
    return (is_wining, wining_combinations)
                
if __name__ == '__main__':
    import doctest
    doctest.testmod()