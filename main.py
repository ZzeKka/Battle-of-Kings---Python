from piece import *
from board import Board
from player import Player




if __name__ == "__main__":
    player_1 = Player('ze', 1)
    player_2 = Player('joao', 2)
    board = Board(player_1,player_2)
    print(board)
    print("Players play each turn write a move with this format: /`")
    while Board.GAME_OVER == False: 
            piece_name, direction = input("Player 1 turn").split()
            if piece_name.lower() == 'k':
                player_1.king.move_piece(board, direction)                     
            elif piece_name.lower() == 'b':
                player_1.barbarian.move_piece(board, direction)
            elif piece_name.lower() == 'w':
                player_1.warrior.move_piece(board, direction)
            elif piece_name.lower() == 'l':
                player_1.lancer.move_piece(board, direction)

            piece_name, direction = input("Player 2 turn").split()
            if piece_name.lower() == 'k':
                player_2.king.move_piece(board, direction)                     
            elif piece_name.lower() == 'b':
                player_2.barbarian.move_piece(board, direction)
            elif piece_name.lower() == 'w':
                player_2.warrior.move_piece(board, direction)
            elif piece_name.lower() == 'l':
                player_2.lancer.move_piece(board, direction)
                
    print("Game Ended")        
                            
        
                
                
        









# '\\' to print a single '\'
""" 
print(f'
               / \\
              | K |   
           - - - - - - 
          | B | W | L |
      - - - - - - - - - - - 
      |   |   |   |   |   |
      - - - - - - - - - - - 
      |   |   |   |   |   |
      - - - - - - - - - - - 
      |   |   |   |   |   |
      - - - - - - - - - - - 
      |   |   |   |   |   |
      - - - - - - - - - - - 
      |   |   |   |   |   |
      - - - - - - - - - - - 
          | L | W | B |  
           - - - - - -
              | K |
               \\ /  
      ') """