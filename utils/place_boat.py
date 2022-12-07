from numpy.random import choice
import utils

def boat_placer(self, position:tuple, length:int):
        """
        From position this function calculates all possible directions where a boat can be headed.
        Once got that, chooses a direction randomly and places the boat in the board.
        Rewrites the board.
        """

        p = position
        l = length - 1
        c = {"N":0, "S":0, "E":0, "W":0} # Coordinates
        
        if utils.neighbor(self, p, 0)[True] == []:
            # -------------------------Vertical axis------------------------
            # SOUTH
            if p[1]+l < 10:
                if utils.neighbor(self, (p[0], p[1]+l, p[2]), 0)[True] == []:
                    c['S'] = 1

            # NORTH
            if p[1]-l >= 0:
                if utils.neighbor(self, (p[0], p[1]-l, p[2]), 0)[True] == []:
                    c['N'] = 1

            # ------------------------Horizontal axis-----------------------
            # EAST
            if p[2]+l < 10:
                if utils.neighbor(self, (p[0], p[1], p[2]+l), 0)[True] == []:
                    c['E'] = 1

            # WEST
            if p[2]-l >= 0:
                if utils.neighbor(self, (p[0], p[1], p[2]-l), 0)[True] == []:
                    c['W'] = 1
                
            # Here compares which direction is equal to True to be listed in "d"
            d = [k for k, v in c.items() if v == True] # Directions

            if d == []:
                return utils.boat_placer(self, utils.rand_point(self), length)
            
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
            return utils.boat_placer(self, utils.rand_point(self), length)