import random

class FifteenPuzzle:
    def __init__(self):
        self.GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
        self.BOARD_SIZE = 4
        self.board = self.initialize_board()
        self.is_over = False

    def number_of_total_inversion_(self, numbers):
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
    
    def position_of_blank_from_bottom_(self, numbers):
        index_of_zero = numbers.index(0)
    
        return self.BOARD_SIZE - int(index_of_zero/self.BOARD_SIZE)
    
    def initialize_board(self):
        pauch = list(range(16)) # Create a set which invovles [0 - 15]
        numbers = random.sample(pauch, 16) # Shuffle the set I've created

        # Calculate number of total inversion
        number_of_total_inversion = self.number_of_total_inversion_(numbers)

        # Calculate position of blank from bottom
        position_of_blank_from_bottom = self.position_of_blank_from_bottom_(numbers)

        numbersTest = list(numbers)
        if (position_of_blank_from_bottom % 2) == (number_of_total_inversion % 2):
            pauch_ = list(pauch) # Create new pauch and remove 0 from it to not chose zero to swap
            index_of_zero = numbers.index(0)
            pauch_.remove(index_of_zero) 
            change_indexes = random.sample(pauch_, 2)
            numbers[change_indexes[0]], numbers[change_indexes[1]] = numbers[change_indexes[1]], numbers[change_indexes[0]]

        return numbers
    
    def turn(self, clicked_index):
        is_game_over = 0
        clicked_index = clicked_index
        zero_index = self.board.index(0)
        possible_moves = [-1, 1, -1*self.BOARD_SIZE, self.BOARD_SIZE]

        # If index of zero is on the top border, remove BOARD_SIZE move from possibles
        if int(zero_index / self.BOARD_SIZE) == 0:
            possible_moves.remove(self.BOARD_SIZE)
        # If index of zero is on the bottom border, remove +BOARD_SIZE move from possibles
        if int(zero_index / self.BOARD_SIZE) == (self.BOARD_SIZE - 1):
            possible_moves.remove(-1*self.BOARD_SIZE)
        # If index of zero is on the left border, remove -1 move from possibles
        if (zero_index % self.BOARD_SIZE) == 0:
            possible_moves.remove(1)
        # If index of zero is on the right border, remove -1 move from possibles
        if (zero_index % self.BOARD_SIZE) == (self.BOARD_SIZE - 1):
            possible_moves.remove(-1)

        # Check if the move is valid
        move = zero_index - clicked_index
        if move not in possible_moves:        
            return False, self.board
        
        # If the move is valid make the move
        self.board[zero_index], self.board[clicked_index] = self.board[clicked_index], self.board[zero_index]

        # Check win condition
        if self.board == self.GOAL_STATE:
            self.is_over = True
            return True, self.board
        
        return True, self.board