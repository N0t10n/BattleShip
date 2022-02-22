from numpy import random, full 

class BattleShip:
    """
    Immutable variables:
        -board: array of shape (2, 10, 10)
        -boats: for key is length and for value, number of boats.
    
    Functions:
        -rand_point: Calculates a random point the array.
        -neighbor: Finds all possible free positions arround the given position argument.
        -direction: Calculates within the board bondaries, all possible directions
                    to locate a boat with length 'length'.
        -rand_direction: With the possible directions extracted from the function 'direction',
                        this function chooses a random direction from the output (list).
        -boat_placer: Rewrites the array board with the placed boat.
        -
        -
        -
    """
    def __init__(self, id=str):
        self.id = id
        self.board = full((2, 10, 10), " ")
        self.boats = {1:4, 2:3, 3:2, 4:1}
    
    def rand_point(self, matrix=0):
        """
        Calculates a random point in the array.

        Parameters:
            -matrix: type int. The matrix where the point is generated.
        
        Return:
            A random point in the given matrix of type tuple.
        """
        point = (matrix,) + tuple(random.randint((self.board.shape[1], self.board.shape[2])))

        if self.board[point] == " ":
            return point
        
        else:
            return BattleShip.rand_point(self)
            
    
    def neighbor(board, position=tuple):
        """
        Finds all possible free positions arround the given position argument.

        Parameters:
            -board: type array. A 3 dimensional matrix.
            -position: type tuple. The position where the function will work on.
        
        Errors:
            -IndexError: if the value position is out of board shape.

        Return:
            A dictionary with the position argument as key,
            and a list of matrices positions of type tuple as value.
        """
        p = position
        pos_list = []
        pos = {}

        try:
            if board[p] == "O":
                # Above
                if p[1] > 0:
                    if board[p[0], p[1]-1, p[2]] == " ":
                        pos_list.append(tuple((p[0],) + (p[1]-1,) + (p[2],)))
                # Below
                if p[1] < 9:
                    if board[p[0], p[1]+1, p[2]] == " ":
                        pos_list.append(tuple((p[0],) + (p[1]+1,) + (p[2],)))
                # Left
                if p[2] > 0:
                    if board[p[0], p[1], p[2]-1] == " ":
                        pos_list.append(tuple((p[0],) + (p[1],) + (p[2]-1,)))
                # Right
                if p[2] < 9:
                    if board[p[0], p[1], p[2]+1] == " ":
                        pos_list.append(tuple((p[0],) + (p[1],) + (p[2]+1,)))
                # Above-right
                if p[1] > 0 and p[2] < 9:
                    if board[p[0], p[1]-1, p[2]+1] == " ":
                        pos_list.append(tuple((p[0],) + (p[1]-1,) + (p[2]+1,)))
                # Above-left
                if p[1] > 0 and p[2] > 0:
                    if board[p[0], p[1]-1, p[2]-1] == " ":
                        pos_list.append(tuple((p[0],) + (p[1]-1,) + (p[2]-1,)))
                # Below-right
                if p[1] < 9 and p[2] < 9:
                    if board[p[0], p[1]+1, p[2]+1] == " ":
                        pos_list.append(tuple((p[0],) + (p[1]+1,) + (p[2]+1,)))
                # Below-left
                if p[1] < 9 and p[2] > 0:
                    if board[p[0], p[1]+1, p[2]-1] == " ":
                        pos_list.append(tuple((p[0],) + (p[1]+1,) + (p[2]-1,)))

                pos[position] = pos_list

                return pos

            else:
                BattleShip.neighbor(board, position)

        except IndexError as ie:
            print(f"""{ie}
            REMEMBER: your board is shape {board.shape}.
                -Your board must have a shape of (2, 10, 10)
                -The position must belong within the board bonds
            """)

    def boat_placer(self, position=tuple, length=int):
        """
        From position this function calculates all possible directions where a boat can be placed.
        Once got that, randomly gets a direction and finally place the boat in the board.

        Return:
            Nothing. Rewrites the self.board
        """
        p = position
        l = length
        c = {"N":0, "S":0, "E":0, "W":0} # Coordinates

        if self.board[p] == " ":
            # Vertical axis
            # Down
            if p[1]+l < 10:
                x = self.board[(0,), p[1]:p[1]+l, p[2]] == " "
                if x.all() == True:
                    c['S'] = 1
            # Up
            if p[1]-l >= 0:
                x = self.board[(0,), p[1]:p[1]-l:-1, p[2]] == " "
                if x.all() == True:
                    c['N'] = 1

            # Horizontal axis
            # Right
            if p[2]+l < 10:
                x = self.board[(0,), p[1], p[2]:p[2]+l] == " "
                if x.all() == True:
                    c['E'] = 1
            # Left
            if p[2]-l >= 0:
                x = self.board[(0,), p[1], p[2]:p[2]-l:-1] == " "
                if x.all() == True:
                    c['W'] = 1
            
            # Here compares which direction is equal to True to be listed in "d"
            d = [k for k, v in c.items() if v == True] # Directions

            if d == []:
                # It's executed is the position doesn't have any possible direction
                return BattleShip.boat_placer(self, BattleShip.rand_point(self), length)

            else:
            # With the all possible directions now randomly stores one of them
                rand_d = random.choice(d)

                # And finally here replaces those free spaces into "O" in the board
                if rand_d == "N":
                    f_p = ((0,), p[1]+1-l, p[2])
                    self.board[(0,), p[1]:p[1]-l:-1, p[2]] = "O"
                elif rand_d == "S":
                    self.board[(0,), p[1]:p[1]+l, p[2]] = "O"
                elif rand_d == "W":
                    f_p = ((0,), p[1], p[2]+1-l)
                    self.board[(0,), p[1], f_p[2]:p[2]+1] = "O"
                else: # d == "E":
                    self.board[(0,), p[1], p[2]:p[2]+l] = "O"

        else:
            # It's executed is the position is already "O"
            return BattleShip.boat_placer(self, BattleShip.rand_point(self), length)

    def shot(self, enemy, difficulty='easy'):
        """
        Description
        """
        # First get the tuple shot
        # shot is an array of two dimensions of type tuple
        if enemy.id != 'Machine':
            if difficulty == 'easy':
                shot = (0,) + tuple(random.randint(self.board.shape[1:]))

                # Writing the shot in the enemys's matrix 0 and to the matrix 1 of the machine
                if enemy.board[shot] == "O": # Boat
                    enemy.board[shot] = "X"
                    self.board[1, shot[1], shot[2]] = "X"

                elif enemy.board[shot] == " ": # Water
                    enemy.board[shot] = "+"
                    self.board[1, shot[1], shot[2]] = "+"

                else: # If it's 'X' or '+'
                    BattleShip.shot(self, enemy)

            else: # Difficulty = 'normal'
                # Code
                pass
            
        else: # If the shooter is the user
            print("Select a position to shoot.")

            # Asking for coordinates
            y = (int(input("Vertical axis:")),)
            x = (int(input("Horizontal axis:")),)
            shot = (0,) + y + x
            print(y + x)

            # Writing the shot in the machine's matrix 0 and to the matrix 1 of the enemy
            if enemy.board[shot] in ['O', " "]:

                if enemy.board[shot] == "O": # Boat
                    enemy.board[shot] = "X"
                    self.board[1, shot[1], shot[2]] = "X"

                else: # Water
                    enemy.board[shot] = "+"
                    self.board[1, shot[1], shot[2]] = "+"

            else:
                print("Coordinates already chosen before, try again.")
                BattleShip.shot(self, enemy)
    
    def boat_placer_loop(self):
        
        # Keys are the boat length and values the number of boats per key
        for k, v in self.boats.items():
            for i in range(v):
                # Random point
                u_p = BattleShip.rand_point(self)
                # Placing it
                BattleShip.boat_placer(self, u_p, k)