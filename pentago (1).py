import numpy as np
import random
#first, we create an empty board
game_board = np.zeros((6, 6))
def display_board(game_board):
    game_board = np.zeros((6, 6))
    pass
    return game_board  
# the rotation function below rotates the respective columns anticlockwise according to the index (k)
# when k=1, it rotates the board 90 degrees anticlockwise when we use the np.rot90 function. 
# to rotate 90 degrees clockwise, set k=3 (3 90 degree anticlockwise turns=1 90 degree clockwise turn)
def apply_move(game_board,turn,row,col,rot):
    game_board_copy = np.copy(game_board)
    game_board_copy[row,col] = turn
    if rot == 1:
        
        game_board_copy[:3,3:6] = np.rot90(game_board_copy[:3,3:6],k=3)
     
    elif rot == 2:
    
        game_board_copy[:3,3:6] = np.rot90(game_board_copy[:3,3:6],k=1)
       
    elif rot == 3: 
       
        game_board_copy[3:6,3:6] = np.rot90(game_board_copy[3:6,3:6],k=3)

    elif rot == 4:
     
         game_board_copy[3:6,3:6] = np.rot90(game_board_copy[3:6,3:6],k=1)
     
    elif rot == 5:
   
        game_board_copy[3:6,:3] = np.rot90(game_board_copy[3:6,:3],k=3)
    
    elif rot == 6:
     
       game_board_copy[3:6,:3] = np.rot90(game_board_copy[3:6,:3],k=1)
     
    elif rot == 7:
  
        game_board_copy[:3,:3] = np.rot90(game_board_copy[:3,:3],k=3)
      
    elif rot == 8:
      
         game_board_copy[:3,:3] = np.rot90(game_board_copy[:3,:3],k=1)
    else:   
        game_board_copy = game_board_copy
    return game_board_copy




# this function is to check which player has occupied the space in the board
def check_move(game_board,row,col):    
    # implement your function here
    move_check = game_board[row,col]
    if move_check == 1:
        print("Player 1 has occupied this position!")
        return False
    elif move_check == 2:
        print("Player 2 has occupied this position!")
        return False
        
    else:
        return True
 
# this function checks for victory before and after rotation, using the check_victory_both function
# this function returns 0 if there is no winning/draw situation for the game
# this function returns 1 if player 1 wins
# this function returns 2 if player 2 wins
# this function returns 3 if the game ends in a draw
def check_victory(game_board,turn,rot):
    game_board_copy = game_board.copy()
       
    if rot == 1:
        game_board_copy[:3,3:6] = np.rot90(game_board_copy[:3,3:6],k=1)
        result_value1 = check_victory_both(game_board_copy, turn, 2, no_of_wins=5)

    elif rot == 2:
        game_board_copy[:3,3:6] = np.rot90(game_board_copy[:3,3:6],k=3)
        result_value1 = check_victory_both(game_board_copy, turn, 1, no_of_wins=5)

    elif rot == 3:
        game_board_copy[3:6,3:6] = np.rot90(game_board_copy[3:6,3:6],k=1)
        result_value1 = check_victory_both(game_board_copy, turn, 4, no_of_wins=5)

    elif rot == 4:
        game_board_copy[3:6,3:6] = np.rot90(game_board_copy[3:6,3:6],k=3)
        result_value1 = check_victory_both(game_board_copy, turn, 3, no_of_wins=5)

    elif rot == 5:
        game_board_copy[3:6,:3] = np.rot90(game_board_copy[3:6,:3],k=1)
        result_value1 = check_victory_both(game_board_copy, turn, 6, no_of_wins=5)

    elif rot == 6:
        game_board_copy[3:6,:3] = np.rot90(game_board_copy[3:6,:3],k=3)
        result_value1 = check_victory_both(game_board_copy, turn, 5, no_of_wins=5)
    elif rot == 7:
        game_board_copy[:3,:3] = np.rot90(game_board_copy[:3,:3],k=1)
        result_value1 = check_victory_both(game_board_copy, turn, 8, no_of_wins=5)

    else:
        game_board_copy[:3,:3] = np.rot90(game_board_copy[:3,:3],k=3)
        result_value1 = check_victory_both(game_board_copy, turn, 7, no_of_wins=5)         
            
    if result_value1 != -1:
        return result_value1 
    else:
        result_value = check_victory_both(game_board, turn, rot, no_of_wins=5)
        if result_value != -1:
            return result_value
        if 0 not in game_board:
            return 3
        
    return 0

# this function  checks the array for 5 in a row (horizontal,diagonal,vertical)
def check_victory_both(game_board,turn,rot, no_of_wins=5):
    
    def winner_check(turn):
        
      
        for i in range(6 - no_of_wins +1):
            for j in range(6):
                victory_checked = True
                for k in range(no_of_wins):
                    if game_board[i+k,j] != turn:
                        victory_checked = False
                        break
                if victory_checked:
            
                    return True
           
              
        
           
            for i in range(6):
                for j in range(6 - no_of_wins +1):
                    victory_checked = True
                    for k in range(no_of_wins):
                        if game_board[i,j+k] != turn:
                           victory_checked = False
                           break
                    if victory_checked:
                        return True
           
            
           
            for i in range(6 -  no_of_wins +1):
                for j in range(6 - no_of_wins +1):
                    victory_checked = True
                    for k in range(no_of_wins):
                        if game_board[i+k,j+k] != turn:
                           victory_checked = False
                           break
                    if victory_checked:
                        return True
            
            
            
            for i in range(6 -  no_of_wins +1):
                for j in range(no_of_wins - 1,6):
                    victory_checked = True
                    for k in range(no_of_wins):
                        if game_board[i+k,j-k] != turn:
                           victory_checked = False
                           break
                    if victory_checked:
                        return True
        return False
      
    if winner_check(1):
      
        return 1
    elif winner_check(2):
        
        return 2
     
    return -1
         
# this function defines possible moves the computer can make at level 1 and level 2 respectively
# at level 1, the computer will do random moves. 
# at level 2, the computer will try to win by calculating moves that can help it win and the player lose
def computer_move(game_board,turn,level):
    if level == 1:
        
        return computermove_random(game_board, turn)
    elif level == 2:
        
        return computermove_level2(game_board, turn)
    else:
        raise ValueError("Invalid input! Only levels 1 and 2 are allowed.")
# this function is for level 1 and hence describes random moves that the computer can make
def computermove_random(game_board, turn):
    row = (random.randint(0, 5))
    col = (random.randint(0, 5))
    rot = (random.randint(1, 8))
    while game_board[row, col] !=0:
       row = (random.randint(0, 5))
       col = (random.randint(0, 5))
       rot = (random.randint(1, 8))
    apply_move(game_board, turn, row, col, rot)
    return row , col , rot
# this function is for level 2 and the computer tries to win by making winning moves or blocking the player from 
# making winning moves.
def computermove_level2(game_board,turn):
    win_moves = [(i,j,rot) 
                 for i in range (6) 
                 for j in range (6) 
                 for rot in range(1,9)
                 if game_board[i,j] == 0 and 
                 check_victory(apply_move(game_board.copy(),turn, i, j, rot), turn, rot) == turn]
  
    avoiding_moves = [(i,j, rot) 
                      for i in range (6) 
                      for j in range (6) 
                      for rot in range (1,9) 
                      if game_board[i,j] == 0 and 
                      check_victory(apply_move(game_board.copy(),turn, i, j, rot), turn, rot) != 3 - turn]
     
    random_moves = [(i,j, rot) 
                    for i in range(6) 
                    for j in range(6) 
                    for rot in range(1,9) 
                    if game_board[i,j] == 0 and (i,j,rot) not in win_moves and (i,j,rot) not in avoiding_moves]
    
    
    try:
        if win_moves:
            print(win_moves)
            move = random.choice(win_moves)
        elif avoiding_moves:
            move = random.choice(avoiding_moves)
        else:
            move = random.choice(random_moves)
    except IndexError:
            raise Exception("No more valid moves.")
    row , col, rot = move 
    print(f"{row} , {col} , {rot}")
    apply_move(game_board, turn, row, col, rot)
    print(game_board)
    return row, col,rot
     
# this is the menu function which will serve as a guide for the player to input their values and understand the game
def menu():  
    # implement your function here
    player = False
    computer = False
    while True:
        print("Welcome to the PENTAGO Game!")
        print("1. Game Instructions  ")
        print("2. Controls ")
        print("3. Multiplayer Mode ")
        print("4. Virtual Opponent vs Player ")
        print("5. Exit Game ")
     
        player_option = int(input("Please enter your option: "))  
        level = 1
        try:
          if player_option == 1:
              print("Each player will take turns to enter row and column numbers from 0 to 5 to place a marble on the board in a round")
              print("0 will correspond to the top first row while 5 will correspond to the bottom last row.")
              print("0 will correspond to the left most column while 5 will correspond to the right most column.")
              print("Player will then select the rotation index from 1 to 8, inclusive of none")
              print("1- Rotate top-right quadrant in the clockwise direction")
              print("2- Rotate top-right quadrant in the counterclockwise direction")
              print("3- Rotate bottom-right quadrant in the clockwise direction")
              print("4- Rotate bottom-right quadrant in the counterclockwise direction")
              print("5- Rotate bottom-left quadrant in the clockwise direction")
              print("6- Rotate bottom-left quadrant in the counterclockwise direction")
              print("7- Rotate top-left quadrant in the clockwise direction")
              print("8- Rotate top-left quadrant in the counterclockwise direction")
              print("A player wins by aligning five or six of his marbles in a vertical, horizontal or diagonal row on the game board. If all 36 spaces on the board are filled without a row of five or six being formed, or if both players form a row of five or six marbales simultaneously in the vertical, horizontal or diagonal row, the games ends in a draw.")
          if player_option == 2:
              print("Row from 0 to 5")
              print("Column from 0 to 5")
              print("Rotation index from 1 to 8")
              print("To end the game, type 'Quit' in any of the inputs for row number, column number and rotation index")
          if player_option == 3:
              print("Multiplayer Version: The game will begin!")
              print("To end the game, type 'Quit'.")
              player = True
          if player_option == 4:
              print("Computer Version: The game will begin!")
              print("To end the game, type 'Quit'.")
              computer = True
          if player_option == 5:
              print("You will exit the game now.")
              break
          
        except Exception as e:
         print("Invalid input! Please the option again within the stated range.")
         
        if player:
             game_board = np.zeros((6,6))
             display_board(game_board)
             print(game_board)
        
             turn = random.choice([1,2])
             row = None
             col = None
             while True:
                 try:
                    row = input("Row for Player %d?(Type 'Quit' to end the game)" %(turn))
                    if row == 'Quit':
                         return menu()
                    row = int(row)
                    if not 0 <= row <=5:
                        print("Invalid input! Please enter a valid integer.")
                        continue
                    col = input("Column for Player %d?(Type 'Quit' to end the game)"%(turn))
                    if col == 'Quit':
                        return menu()
                    col= int(col)
                    if not 0<= col <=5 :
                        print("Invalid input! Please enter a valid integer.")
                        continue
              
                    if check_move(game_board, row, col)== True:
                        print(apply_move(game_board, turn, row, col, None))
                        rot  = input("Rotation Index for Player %d?(Type 'Quit' to end the game)" %(turn))
                        rot = int(rot)
                        if 1<= int(rot) <= 8:
                            #print(apply_move(game_board, turn, row, col, rot))
                            game_board = apply_move(game_board, turn, row, col, rot)
                            print(game_board)
                            victory_checked = check_victory(game_board, turn, rot)
                            if victory_checked == 1:
                              print("Congratualations! Player 1 has won the game.")
                              break
                            elif victory_checked == 2:
                               print("Congratulations! Player 2 has won the game.")
                               break
                            elif victory_checked == 3:
                               print("The game has come to a draw.")
                               break
                            turn = 3 - turn
                            continue
                        elif rot == 'Quit':
                             return menu()
                        while not 1<= int(rot) <= 8:
                           print('Invalid index')
                           rot  = input("Rotation Index for Player %d?(Type 'Quit' to end the game)" %(turn))
                           if rot == 'Quit':
                            return menu()
                    else:
                        print("Invalid Input! Please enter a value within the stated range.")
                        continue

                     
                     
                     
                 except ValueError:
                     print("Invalid Input! Please enter a value within the stated range.")
                 
          
             
            
              
             print("The game Pentago has ended! Thank you for playing!")
             player = False
                
        elif computer== True :
              game_board = np.zeros((6,6))
              display_board(game_board)
              print(game_board)
         
              while True:
                    try:
                      level = int(input("Diffculty: Level 1 or Level 2 "))
                      if level == 1 or level == 2:
                          break
                      if level.isdigit()== False:
                          if int(level) != 1 and int(level)!=2:
                             print ('Input either Level 1 or Level 2')
                          else:
                            break
                    except Exception as e:
                        print("Invalid input! Please enter either 1 or 2.")
              turn = 1
              while True: 
                 if turn == 1:
                     row = None
                     col = None
                     try:
                        row = input("Row for Player %d?(Type 'Quit' to end the game)" %(turn))
                        if row == 'Quit':
                             return menu()
                        row = int(row)
                        if not 0 <= row <=5:
                            print("Invalid input! Please enter a valid integer.")
                            continue
                        col = input("Column for Player %d?(Type 'Quit' to end the game)"%(turn))
                        if col == 'Quit':
                            return menu()
                        col= int(col)
                        if not 0<= col <=5 :
                            print("Invalid input! Please enter a valid integer.")
                            continue
                  
                        if check_move(game_board, row, col)== True:
                            print(apply_move(game_board, turn, row, col, None))
                            rot  = input("Rotation Index for Player %d?(Type 'Quit' to end the game)" %(turn))
                            rot = int(rot)
                            if 1<= int(rot) <= 8:
                                #print(apply_move(game_board, turn, row, col, rot))
                                game_board = apply_move(game_board, turn, row, col, rot)
                                print(game_board)
                                victory_checked = check_victory(game_board, turn, rot)
                                if victory_checked == 1:
                                  print("Congratualations! Player 1 has won the game.")
                                  break
                                elif victory_checked == 2:
                                   print("Congratulations! Player 2 has won the game.")
                                   break
                                elif victory_checked == 3:
                                   print("The game has come to a draw.")
                                   break
                                turn = 3 - turn
                                
                            elif rot == 'Quit':
                                 return menu()
                            while not 1<= int(rot) <= 8:
                               print('Invalid index')
                               rot  = input("Rotation Index for Player %d?(Type 'Quit' to end the game)" %(turn))
                               if rot == 'Quit':
                                return menu()
                        else:
                            print("Invalid Input! Please enter a value within the stated range.")
                            continue
                           
                     except ValueError:
                         print("Invalid Input! Please enter a value within the stated range.")
                         
                     
                 if turn == 2:
                     try: 
                        print("computer is making a move.")
                        row, col, rot = computer_move(game_board, turn, level)
                        print(row,col,rot)
                        print(apply_move(game_board, turn, row, col, None))
                       
                        
                        print("Rotating")
                        game_board = apply_move(game_board, turn, row, col, rot)
                        print(game_board)
                        victory_checked = check_victory(game_board, turn, rot)
                             
                        if victory_checked == 1:
                             print("Congratulations! You won.")
                             break
                        elif victory_checked ==2:
                             print("Computer has won.")
                             break
                        elif victory_checked == 3:
                             print("The game has come to a draw.")
                             break
                        print("It is your turn.")
                        turn = 3 - turn
                     except Exception as e:
                        print("Error occured during computer's move:". str(e))
                       
                     
             
                 
                         
    else: 
               print("The game has ended. Thank you for playing!")       
               return computer == False
                           
if __name__ == "__main__":
    menu()
   