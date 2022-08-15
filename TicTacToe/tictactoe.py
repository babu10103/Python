import time
import math
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer

board = [[' ']*3 for _ in range(3)]
class TicTacToe():
  def __init__(self):
    self.board = self.make_board()
    self.current_winner = None

  @staticmethod
  def make_board():
    return [' ' for _ in range(9)]

  def print_board(self):
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ', ' | '.join(row), ' |')

  @staticmethod
  def print_board_nums():
    number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
    for row in number_board:
      print('| ', ' | '.join(row), ' |')
  def make_move(self, square, letter):
    if self.board[square] == ' ':
      self.board[square] = letter
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False
  def winner(self, square, letter):
    row_ind = square//3
    col_ind = square%3

    row = self.board[3*row_ind:(row_ind+1) * 3]
    if all([s == letter for s in row]):
      return True
    col = [self.board[col_ind + i * 3] for i in range(3)]
    if all([s == letter for s in col]):
      return True
    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      if all([s == letter for s in diagonal1]):
        return True
      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      if all([s == letter for s in diagonal2]):
        return True
    return False
  def empty_squares(self):
    return ' ' in self.board
  def num_empty_squares(self):
    return self.board.count(' ')
  def available_moves(self):
    # return [i for i in range(9) if self.board[i] == ' ']
    # or
    return [i for i, x in enumerate(self.board) if x == " "]

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')



    

if __name__ == '__main__':
  x_player = SmartComputerPlayer('X')
  o_player = HumanPlayer('O')
  t = TicTacToe()
  play(t, x_player, o_player, print_game=True)








  # def uphill_check(self):
  #   return board[0][2] == board[1][1] and board[1][1] == board[2][0]
  # def downhill_check(self):
  #   return board[0][0] == board[1][1] and board[1][1] == board[2][2]
  # def row_check(self, i):
  #   return board[i][0] == board[i][1] and board[i][1] == board[i][2]
  # def col_check(self, j):
  #   return board[0][j] == board[1][j] and board[1][j] == board[2][j]
    
  # def check_for_win(self, i, j):
  #   if (i == 0 and j == 2) or (i == 2 and j == 0) :
  #     return self.uphill_check() or self.row_check(i) or self.col_check(j)
  #   elif (i == 0 and j == 0) or (i == 2 and j == 2):
  #     return self.downhill_check() or self.row_check(i) or self.col_check(j)
  #   elif i == 1 and j == 1:
  #     return self.uphill_check() or self.downhill_check() or self.row_check(i) or self.col_check(j)
  #   return self.row_check(i) or self.col_check(j)
    
  # def set_char(self, i, j):
  #   while(board[i][j] != ' '):
  #     k, l = input('Please enter a valid cell position: ').split()
  #     i, j = int(k), int(l)

  #   board[i][j] = self.letter
  #   if self.check_for_win(i, j):
  #     print(self.name, 'won')
