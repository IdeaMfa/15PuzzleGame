import random

GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
BOARD_SIZE = 4

def test_initialization():
    NUMBER_OF_TEST_CASES = 500
    okay = 0
    not_okay = 0
    for i in range(NUMBER_OF_TEST_CASES):
        board = initialize_board()
        position_of_blank_from_bottom = position_of_blank_from_bottom_(board) # Calculate position of blank from bottom
        number_of_total_inversion = number_of_total_inversion_(board) # Calculate number of total inversion
        if (position_of_blank_from_bottom % 2) == (number_of_total_inversion % 2):
            not_okay += 1
        else:
            okay += 1

    print(f"Passed: {okay}, Not passed: {not_okay}")

def print_board(board):
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            print(f"  {board[i*BOARD_SIZE + j]}", end="")
        print()

def number_of_total_inversion_(numbers):
    numbers_without_zero = list(numbers)
    numbers_without_zero.remove(0)
    number_of_total_inversion = 0
    length = len(numbers_without_zero)
    for i in range(length - 1):
        number_of_inversion = 0
        for j in range(i+1, length):
            if (numbers_without_zero[i] > numbers_without_zero[j]):
                number_of_inversion += 1
        number_of_total_inversion += number_of_inversion
    
    return number_of_total_inversion

def position_of_blank_from_bottom_(numbers):
    index_of_zero = numbers.index(0)
    
    return 4 - int(index_of_zero/4)


def initialize_board():
    pauch = list(range(16)) # Create a set which invovles [0 - 15]
    numbers = random.sample(pauch, 16) # Shuffle the set I've created

    # Calculate number of total inversion
    number_of_total_inversion = number_of_total_inversion_(numbers)

    # Calculate position of blank from bottom
    position_of_blank_from_bottom = position_of_blank_from_bottom_(numbers)

    numbersTest = list(numbers)
    if (position_of_blank_from_bottom % 2) == (number_of_total_inversion % 2):
        pauch_ = list(pauch) # Create new pauch and remove 0 from it to not chose zero to swap
        index_of_zero = numbers.index(0)
        pauch_.remove(index_of_zero) 
        change_indexes = random.sample(pauch_, 2)
        numbers[change_indexes[0]], numbers[change_indexes[1]] = numbers[change_indexes[1]], numbers[change_indexes[0]]

    return numbers


test_initialization()

def turn(board, clicked):
    is_game_over = 0
    clicked_index = clicked
    zero_index = board.index(0)
    possible_moves = [-1, 1, -1*BOARD_SIZE, BOARD_SIZE]

    # If index of zero is on the top border, remove BOARD_SIZE move from possibles
    if int(zero_index / BOARD_SIZE) == 0:
        possible_moves.remove(BOARD_SIZE)
    # If index of zero is on the bottom border, remove +BOARD_SIZE move from possibles
    if int(zero_index / BOARD_SIZE) == (BOARD_SIZE - 1):
        possible_moves.remove(-1*BOARD_SIZE)
    # If index of zero is on the left border, remove -1 move from possibles
    if (zero_index % BOARD_SIZE) == 0:
        possible_moves.remove(1)
    # If index of zero is on the right border, remove -1 move from possibles
    if (zero_index % BOARD_SIZE) == (BOARD_SIZE - 1):
        possible_moves.remove(-1)

    move = zero_index - clicked_index
    if move not in possible_moves:        
        return 0, board
    
    board[zero_index], board[clicked_index] = board[clicked_index], board[zero_index]

    if board == GOAL_STATE:
        return 2, board
    
    return 1, board

def game_loop():
    board = initialize_board()
    print("Your board: ")

    while (True):
        print_board(board)
        clicked_index = int(input("Click index: "))
        status_after_move = turn(board, clicked_index)
        if status_after_move[0] == 0:
            print("Move is not possible")
        if status_after_move[0] == 2:
            print_board(status_after_move[1])
            break
        board =status_after_move[1]


game_loop()