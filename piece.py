information = {
    'K' : ['King','1','This piece has no attacks'],
    'B' : ['Barbarian','2', 'ENERGY RUPTURE -> Attacks in both diagonals until it reaches the end of the board'],
    'W' : ['Warrior', '3', 'SWORD CYCLONE -> Attacks in all 9 sqaures around him'],
    'L' : ['Lancer', '3', 'SWIPE & THRUST -> Attackes 1 square in 2 front diagonals and 2 squares to the front']
    
} 

class Piece: 
    def __init__(self, x, y, player, health, board_symbol):
        self.x = x
        self.y = y
        self.player = player
        self.health = health
        self.board_symbol = board_symbol
       
        
        
    #prints the information of a Piece
    def __str__(self):
        return(f"""\n
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
        Piece Name: {information[self.board_symbol][0]}
        Current Position: ({self.x},{self.y})
        Current HP: {self.health}
        Attack: {information[self.board_symbol][2]}
    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n""")  
    
    #function that moves pieces, they can move up, down, left, right and returns true or false depending if the move was successfull or not
    #[complete] - need to develop attack now
    def move_piece(self, board, move):
        
        if move.lower() == 'down':
            new_x = self.x + 1
            if board.check_if_position_valid(new_x, self.y):
                board.initial_board[new_x][self.y] = board.initial_board[self.x][self.y]
                board.initial_board[self.x][self.y] = 'Free'
                self.x = new_x
                if(self.board_symbol != 'K'):
                    self.attack(board) #attack
                print(board)
                return True
                
        elif move.lower() == 'up':
            new_x = self.x - 1
            if board.check_if_position_valid(new_x, self.y):
                board.initial_board[new_x][self.y] = board.initial_board[self.x][self.y]
                board.initial_board[self.x][self.y] = 'Free'
                self.x = new_x
                if(self.board_symbol != 'K'):
                    self.attack(board) #attack
                print(board)
                return True
        
            
        elif move.lower() == 'left':
            new_y = self.y - 1
            if board.check_if_position_valid(self.x, new_y):
                board.initial_board[self.x][new_y] = board.initial_board[self.x][self.y]
                board.initial_board[self.x][self.y] = 'Free'
                self.y = new_y
                if(self.board_symbol != 'K'):
                    self.attack(board) #attack
                print(board)
                return True
             
        
        elif move.lower() == 'right':
            new_y = self.y + 1
            if board.check_if_position_valid(self.x, new_y):
                board.initial_board[self.x][new_y] = board.initial_board[self.x][self.y]
                board.initial_board[self.x][self.y] = 'Free'
                self.y = new_y
                if(self.board_symbol != 'K'):
                    self.attack(board) #attack
                print(board)
                return True
            
            
        else:
            print('Move not valid')
            return False 
    
    def attack_square(self, x, y,agressor_player, board):
        #exception takes care of a square that is out of the border
        #print(f"({x},{y}) --- {board.initial_board[x][y]}")
        
        attacked_piece = board.initial_board[x][y] #piece object 
        if board.initial_board[x][y] != 'Free' and board.initial_board[x][y] is not None and agressor_player != attacked_piece.player:
            print('Piece was hit!')
            board.piece_hit(attacked_piece)
        else:
            #print('No hit')
            ...
    
        
    def display_pos(self):
        print(f'({self.x}, {self.y})')

        
"""
King
"""        
class King (Piece):
    SYMBOL = 'K'
    
    def __init__(self,x, y, player, is_alive=True):
        super().__init__(x, y, player, health=1,board_symbol=King.SYMBOL)
        self.is_alive = is_alive
    
    
        
        
"""
Barbarian
"""              
class Barbarian (Piece):
    SYMBOL = 'B'
    
    def __init__(self, x, y, player):
        super().__init__(x, y, player, health=2,board_symbol=Barbarian.SYMBOL)

    def attack(self, board):
        print("Energy Rupture unleashed")
        invert_x = 1
        if self.player == 2:
            invert_x = -1
        
        for i in range(1,5):
            current_x = self.x + (i * invert_x)
            current_y = self.y + i
            if(current_x < 0 or current_y < 0):
                break
            try:
                super(Barbarian, self).attack_square(current_x,current_y,self.player,board)
            except:
                break
            
            
        for i in range(1,5):
            current_x = self.x + (i * invert_x)
            current_y = self.y - i
            
            #fixes python -1 indexes
            if(current_x < 0 or current_y < 0):
                break
            
            #exception prevent out of index range error
            try:
                super(Barbarian, self).attack_square(current_x,current_y,self.player,board)
            except:
                break                  
"""
Warrior
"""          
class Warrior (Piece):
    SYMBOL = 'W'
    
    def __init__(self, x, y, player):
        super().__init__(x, y, player, health=3,board_symbol=Warrior.SYMBOL)
    
    def attack(self, board):
        #attacks 9 squares around piece
        print("Warrior started Sword Cyclone")
        
        #vertical
        current_x = self.x - 1 
        if( not(current_x < 0 or self.y < 0)):
            try:
                super(Warrior, self).attack_square(current_x,self.y,self.player, board)
            except:
                ...
        
        current_x = self.x + 1 
        if(not (current_x < 0 or self.y < 0)):
            try:
                super(Warrior, self).attack_square(current_x,self.y,self.player, board)
            except:
                ...
                
        #horizontal
        current_y = self.y - 1 
        if(not(self.x < 0 or current_y < 0)):
            try:
                super(Warrior, self).attack_square(self.x,current_y,self.player, board)
            except:
                ...
        
        current_y = self.y + 1 
        if(not(self.x < 0 or current_y < 0)):
            try:
                super(Warrior, self).attack_square(self.x,current_y,self.player, board)
            except:
                ...
                
        #diagonal
        current_x = self.x + 1
        current_y = self.y + 1 
        if(not(current_x < 0 or current_y < 0)):
            try:
                super(Warrior, self).attack_square(current_x,current_y,self.player, board)
            except:
                ...
        
        current_x = self.x - 1
        current_y = self.y + 1 
        if(not(current_x < 0 or current_y < 0)):
            try:
                super(Warrior, self).attack_square(current_x,current_y,self.player, board)
            except:
                ...
                
        current_x = self.x + 1
        current_y = self.y - 1 
        if(not(current_x < 0 or current_y < 0)):
            try:
                super(Warrior, self).attack_square(current_x,current_y,self.player, board)
            except:
                ...
        
        current_x = self.x - 1
        current_y = self.y - 1 
        if(not(current_x < 0 or current_y < 0)):
            try:
                super(Warrior, self).attack_square(current_x,current_y,self.player, board)
            except:
                ...
        

   
"""
Lancer
"""          
class Lancer (Piece):
    SYMBOL = 'L'
    
    def __init__(self, x, y, player):
        super().__init__(x, y, player, health=2,board_symbol=Lancer.SYMBOL)
        
    def attack(self, board):
        print('Lancer started rampaging')
        invert_x = 1
        if (self.player == 2):
            invert_x = -1
        
        #thrust (2 squares in front)
        for i in range(1,3):
            current_x = self.x + (i * invert_x)
            if(current_x < 0 or self.y < 0):
                break
            try:
                super(Lancer, self).attack_square(current_x,self.y,self.player,board)
            except:
                break
                ...
                
        #swipe
        current_x = self.x + (1 * invert_x)
        current_y = self.y + 1 
        if(not(current_x < 0 or current_y < 0)):
            try:
                super(Lancer, self).attack_square(current_x,current_y,self.player, board)
            except:
                ...
                
        current_x = self.x + (1 * invert_x)
        current_y = self.y - 1 
        if(not(current_x < 0 or current_y < 0)):
            try:
                super(Lancer, self).attack_square(current_x,current_y,self.player, board)
            except:
                ...
        