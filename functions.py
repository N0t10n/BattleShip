from numpy import random, full, array2string
from random import choice

class BattleShip:
    """
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

    def __init__(self, id=str, difficulty=None):
        self.id = id
        self.life = 20 # Total number of boat cells
        self.board = full((2, 10, 10), " ")
        self.boats = {4:1, 3:2, 2:3, 1:4}
        self.difficulty = difficulty
    
    def rand_point(self, matrix=0):
        """
        Calculates a random point in the array.
        Return a position of type tuple.
        """
        point = (matrix,) + tuple(random.randint((self.board.shape[1], self.board.shape[2])))

        if self.board[point] == " ":
            return point
        
        else:
            return BattleShip.rand_point(self)
            
    
    def neighbor(self, position=tuple, level=int):
        """
        Find all possible free positions arround the given positional argument.
        Return a dictionary with occupied positions in True and free in False.
        """
        p = position
        pos_dict = {True: 0, False: 0}
        true = []
        false = []

        # Above
        if p[1] > 0:
            pos = (level,) + (p[1]-1,) + (p[2],)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Below
        if p[1] < 9:
            pos = (level,) + (p[1]+1,) + (p[2],)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Left
        if p[2] > 0:
            pos = (level,) + (p[1],) + (p[2]-1,)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Right
        if p[2] < 9:
            pos = (level,) + (p[1],) + (p[2]+1,)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Above-right
        if p[1] > 0 and p[2] < 9:
            pos = (level,) + (p[1]-1,) + (p[2]+1,)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Above-left
        if p[1] > 0 and p[2] > 0:
            pos = (level,) + (p[1]-1,) + (p[2]-1,)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Below-right
        if p[1] < 9 and p[2] < 9:
            pos = (level,) + (p[1]+1,) + (p[2]+1,)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        # Below-left
        if p[1] < 9 and p[2] > 0:
            pos = (level,) + (p[1]+1,) + (p[2]-1,)
            if self.board[pos] == " ":
                false.append(pos)
            else:
                true.append(pos)

        pos_dict[True] = true
        pos_dict[False] = false

        return pos_dict


    def boat_placer(self, position=tuple, length=int):
        """
        From position this function calculates all possible directions where a boat can be headed.
        Once got that, chooses a direction randomly and places the boat in the board.
        Rewrites the board.
        """
        p = position
        l = length - 1
        c = {"N":0, "S":0, "E":0, "W":0} # Coordinates
        
        if BattleShip.neighbor(self, p, 0)[True] == []:
            # Vertical axis
            # SOUTH
            if p[1]+l < 10:
                if BattleShip.neighbor(self, (p[0], p[1]+l, p[2]), 0)[True] == []:
                    c['S'] = 1

            # NORTH
            if p[1]-l >= 0:
                if BattleShip.neighbor(self, (p[0], p[1]-l, p[2]), 0)[True] == []:
                    c['N'] = 1

            # Horizontal axis
            # EAST
            if p[2]+l < 10:
                if BattleShip.neighbor(self, (p[0], p[1], p[2]+l), 0)[True] == []:
                    c['E'] = 1

            # WEST
            if p[2]-l >= 0:
                if BattleShip.neighbor(self, (p[0], p[1], p[2]-l), 0)[True] == []:
                    c['W'] = 1
                
            # Here compares which direction is equal to True to be listed in "d"
            d = [k for k, v in c.items() if v == True] # Directions

            if d == []:
                return BattleShip.boat_placer(self, BattleShip.rand_point(self), length)
            
            else:
                o = choice(d)
                
                if o == "N":
                    self.board[0, p[1]-l:p[1]+1, p[2]] = "O"

                elif o == "S":
                    self.board[0, p[1]:p[1]+l+1, p[2]] = "O"

                elif o == "W":
                    self.board[0, p[1], p[2]-l:p[2]+1] = "O"

                else: # d == "E":
                    self.board[0, p[1], p[2]:p[2]+l+1] = "O"
        else:
            return BattleShip.boat_placer(self, BattleShip.rand_point(self), length)


    def machine_shot(self, enemy, difficulty, around=None):
        """
        description
        """
        p = (0,) + tuple(random.randint(self.board.shape[1:]))

        if difficulty == 'easy':

            if enemy.board[p] == "O": # Boat
                enemy.board[p] = "X"
                enemy.life -= 1
                self.board[1, p[1], p[2]] = "X"
                return BattleShip.machine_shot(self, enemy, difficulty, around)

            elif enemy.board[p] == " ": # Water
                enemy.board[p] = "+"
                self.board[1, p[1], p[2]] = "+"

            else: # If it's 'X' or '+'
                return BattleShip.machine_shot(self, enemy, difficulty, around)
        
        elif difficulty == 'normal':

            if type(around) == None:

                if enemy.board[p] == "O": # Boat
                    enemy.board[p] = "X"
                    enemy.life -= 1
                    self.board[1, p[1], p[2]] = "X"

                    # Finding empty spots around
                    list_shot = BattleShip.neighbor(self, p, 1)[False]
                    ar = choice(list_shot)
                    return BattleShip.machine_shot(self, enemy, difficulty, ar)

                elif enemy.board[p] == " ": # Water
                    enemy.board[p] = "+"
                    self.board[1, p[1], p[2]] = "+"

                else: # If it's 'X' or '+'
                    return BattleShip.machine_shot(self, enemy, difficulty, around)

            else: # If around is tuple -> a position around the hit
                if enemy.board[around] == "O": # Boat
                    enemy.board[around] = "X"
                    enemy.life -= 1
                    self.board[1, around[1], around[2]] = "X"
                    return BattleShip.machine_shot(self, enemy, difficulty, around)

                elif enemy.board[around] == " ": # Water
                    enemy.board[around] = "+"
                    self.board[1, around[1], around[2]] = "+"

                else: # If it's 'X' or '+'
                    return BattleShip.machine_shot(self, enemy, difficulty, around)

        else: # difficulty == 'god':
            pass
        

    def user_shot(self, enemy, position=tuple):
        """
        description
        """
        p = position

        if enemy.board[p] in ['O', " "]:

            if enemy.board[p] == "O": # Boat
                enemy.board[p] = "X"
                enemy.life -= 1
                self.board[1, p[1], p[2]] = "X"
                return print(f'You reached the opponent!'), BattleShip.user_shot(self, enemy, position)

            else: # Water
                enemy.board[p] = "+"
                self.board[1, p[1], p[2]] = "+"

        else:
            print("Coordinates already chosen before, try again.\n")
            return BattleShip.user_shot(self, enemy, position)


    def shooting(self, enemy, difficulty=None, around=None):
        """
        Description
        """
        c_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        
        if enemy.id != 'Machine': # If the shooter is the machine
            return BattleShip.machine_shot(self, enemy, difficulty, around)
            
        else: # If the shooter is the user
            print("Select a position to shoot.")

            # Asking for coordinates
            x_str = input("\tHorizontal axis: ").upper()
            x = 0
            y = 0

            ## EASTER EGG
            if x_str == "NUKE":
                self.board[1, :, :] = 'X'
                self.board_printer()
                print('\nBoOoOoOoOoOoOoM!\n')
                enemy.life = 0
            ## END EASTER EGG

            elif x_str in c_x:
                x = (c_x.index(x_str),)
                y = (int(input("\tVertical axis: ")) - 1,)

            else:
                print('\nYou typed a wrong character.')
                return BattleShip.shooting(self, enemy)

            shot = (0,) + x + y
            print(f'{c_x[x[0]]}, {y[0]+1}')

            return BattleShip.user_shot(self, enemy, shot)


    def boat_placer_loop(self):
        """
        The function to gather the neccesary functions and loop them
        for every type of boat.
        """
        # Keys are the boat length and values the number of boats per key
        for k, v in self.boats.items():
            for i in range(v):
                # Random point
                u_p = BattleShip.rand_point(self)
                # Placing it
                BattleShip.boat_placer(self, u_p, k)


    def board_printer(self):
        """
        A function to convert the board array into a string and be able to polish it and
        give color to specific characters.
        """
        c_x = ['   1' , '  2', '  3', '  4', '  5', '  6', '  7', '  8', '  9', '  10']
        c_y = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        # Splitting the board by two
        p_board = array2string(self.board)[2:-2].split('\n')
        above = p_board[:10]
        under = p_board[11:]

        # Top board
        for r in above:
            r = r.strip()[1:-1].replace(']', '')
            for i in r:
                # Turn to red
                if i == 'X':
                    r = r.replace(i, '\033[91m'+i+'\033[0m')
                # Turn to blue
                if i == '+':
                    r = r.replace(i, '\033[94m'+i+'\033[0m')
            print('  '+r)

        print()

        # Bottom board
        print(*c_x) # Printing numbers
        for r, e in zip(under, c_y):
            r = r.strip()[1:-1].replace('[', '')
            for i in r:
                # Turn to red
                if i == 'X':
                    r = r.replace(i, '\033[91m'+i+'\033[0m')
                # Turn to blue
                if i == '+':
                    r = r.replace(i, '\033[94m'+i+'\033[0m')
            print(e, r)