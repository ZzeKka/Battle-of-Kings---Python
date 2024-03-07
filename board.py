from piece import *

class Board:
    
    GAME_OVER = False
    
    def __init__(self, player_1, player_2):
        #Player 1 Pieces
        p1_K = player_1.king
        p1_B = player_1.barbarian
        p1_W = player_1.warrior
        p1_L = player_1.lancer
        
        #Player 2 Pieces
        p2_K = player_2.king
        p2_B = player_2.barbarian
        p2_W = player_2.warrior
        p2_L = player_2.lancer
        
        self.initial_board = [
                      [ None , None , p1_K , None , None ],
                      [ None , p1_B , p1_W , p1_L , None ], 
                      ['Free','Free','Free','Free','Free'],
                      ['Free','Free','Free','Free','Free'],
                      ['Free','Free','Free','Free','Free'],
                      ['Free','Free','Free','Free','Free'],
                      [ None , p2_L , p2_W , p2_B , None ],
                      [ None , None , p2_K , None , None ]]
    
    #method that prints current board
    def __str__(self):
        
        board_display = f""""""
        
        #1st line
        board_display += '         / \\         \n'
        board_display += self.draw_one_square_line(0)    
        board_display += '     - - - - - -     \n'
        
        #2nd line
        board_display += self.draw_three_square_line(1)
        board_display += '- - - - - - - - - - -\n'
        
        #3th line to 6th line
        board_display += self.draw_five_square_lines(2,4)
            
        #7th line
        board_display += self.draw_three_square_line(6)
        board_display += '     - - - - - -     \n'
        
        #8th line    
        board_display += self.draw_one_square_line(7)
        board_display += '         \\ /         \n'
        
        return board_display

    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    #Draw board line methods
    """
        Those 3 functions are responsible for helping draw the board
        Arguments: 
        line_number : ith number of the board
    """
    
    def draw_one_square_line(self, line_number):
        line = f''
        if not isinstance(self.initial_board[line_number][2], str) and self.initial_board[line_number][2] is not None:
            line += f"""        | {self.initial_board[line_number][2].board_symbol} |        \n"""
        else:
            line += f"""        |   |        \n"""    
        return line
      
    
    def draw_three_square_line(self, line_number):  
        line = '    |'
        for i in range(3):
            if not isinstance(self.initial_board[line_number][i+1], str) and self.initial_board[line_number][i+1] is not None:
                line += f""" {self.initial_board[line_number][i+1].board_symbol} |"""
            else:
                line += f"""   |"""
        line += '\n'
        return line
    
    def draw_five_square_lines(self, first_line_number, number_of_lines):
        line = f''
        for i in range (number_of_lines): 
            line += '|'       
            for j in range(5):
                if not isinstance(self.initial_board[i+first_line_number][j], str) and self.initial_board[i+first_line_number][j] is not None:
                    line += f""" {self.initial_board[i+first_line_number][j].board_symbol} |"""
                else:
                    line += f"""   |"""
            
            line += '\n- - - - - - - - - - -\n'
        return line
    
    # * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
    
    #check if position is inside the board
    def check_if_position_valid(self, x, y):
        return ((x < len(self.initial_board)) and (y < len(self.initial_board[0])) and (self.initial_board[x][y] == 'Free'))
    
    #piece hit, loses 1hp
    def piece_hit(self, attacked_piece):
        attacked_piece.health -= 1
        self.check_if_piece_alive(attacked_piece)

    
    #after piece was hit check if its alive or her current health
    def check_if_piece_alive(self, piece):
        piece_type = information[piece.board_symbol][0]
        if piece.health == 0 and piece.board_symbol == 'K':
            print(f'player {piece.player} King was detrowned')
            self.initial_board[piece.x][piece.y] = 'Free'
            if piece.player == 1:
                print(f'Congratilanions Player 2 You won the Game!!!')
            else:
                print(f'Congratilanions Player 1 You won the Game!!!')
            self.game_ended()
        elif piece.health == 0:
            #if piece was King end game    
            print(f'player {piece.player} {piece_type} was killed and removed from the board')
            self.initial_board[piece.x][piece.y] = 'Free'        
        else:
            print(f'player {piece.player} {piece_type} current health is {piece.health}')
            
    def game_ended():
       Board.GAME_OVER = True 
                

    
        