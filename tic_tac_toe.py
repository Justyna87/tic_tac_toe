import random
def player_move(board):  #this function works perfectly :)
    position =int(input("which position do you want to move? "))
    if position>=0 and position <20:
      while board[position] != "-":
        print("the position is occupied, enter the number once more")
        position =int(input())

      board = board[:position]+ board[position:].replace(board[position], "x", 1)
      print(board, "\n")
    else:
      board = board[:position]+ board[position:].replace(board[position], "x", 1)
      print(board)
    return board

def pc_move(board): # # Returns a game board with the computer's move.
  position_pc = random.randrange(0, 20)
  print("pc position is:", position_pc, "\n")
  if board[position_pc] != "-":
    while board[position_pc] != "-":  #
        position_pc = random.randrange(0, 20)
        print("there is already a mark, new pc position is:", position_pc)

    board = board[:position_pc]+ board[position_pc:].replace(board[position_pc], "o", 1)
    print(board, "\n")
  else:
       board = board[:position_pc]+ board[position_pc:].replace(board[position_pc], "o", 1)
       print(board)
  return board

def evaluate (board): # checks the board, if it is full, not full, somebody won?
 if x_won in board:
   print("x won")  #if true - must be stopped
   return True
 elif o_won in board:
   print("o won") # if true -must be stopped
   return True
 elif element3 not in board:
   print("board is full, end of the game \n")  # if true - must be stopped
   return True
 else:
   print("\n")
   return False

board = 20 * "-"
x_won = "xxx"
o_won ="ooo"
element3 = "-"
print("This is the board field:\n", board)
print("Choose the number between 0 and 19")
while evaluate(board)==False: #as long as no one won, the game will be continued
    board = player_move(board)
    board = pc_move(board)