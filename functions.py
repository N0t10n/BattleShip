import numpy as np

class BattleShip:

    def __init__(self, id):
        self.id = id
    
    def rand_point(board, matrix=int):
        """
        Calculates a random point the array.

        Parameters:
            -board: type array. A 3 dimensional matrix.
            -matrix: type int. The matrix where the point is generated.
        
        Errors:
            -matrix value out of bounds
            -board type not array
            -board dimensions not equal to two

        Return:
            Returns a random point in the given matrix of type tuple.
        """
        try:
            if int(matrix) < board.shape[0]:
                point = tuple(np.random.randint((board.shape[1]+1, board.shape[2]+1)))
            
            return (int(matrix),) + point

        except UnboundLocalError as uble:
            print(f"""{uble}
                Possible errors:
                    -Matrix value out of bounds
                    -Board type not array
                    -Board dimensions not equal to two
            """)
    
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

        except IndexError as ie:
            print(f"""{ie}
                REMEMBER: your board is shape {board.shape}.
                    -Your board must have a shape of (2, 10, 10)
                    -The position must belong within the board bonds
            """)

    def direction(board, position=tuple, length=int):
        """
        Calculates within the board bondaries, all possible directions
        to locate a boat with length 'length'.

        Parameters:
            -board: type array. A 3 dimensional matrix
            -position: type tuple. The start boat coordinates.
            -length: boat length as integer.

        Return:
            A list of all possible directions mentioned:
            North, South, West, East
        """
        p = position
        l = int(length - 1)
        c = {"N":0, "S":0, "E":0, "W":0}

        try:
            if l > 0:
                if board[p] != "O":
                    # Vertical axis
                    # Down
                    if p[1]+l < 10:
                        x = board[p[0], p[1]:p[1]+l, p[2]] == " "
                        for i in x:
                            if i == True:
                                c['S'] += 1
                    # Up
                    if p[1]-l >= 0:
                        x = board[p[0], p[1]:p[1]-l:-1, p[2]] == " "
                        for i in x:
                            if i == True:
                                c['N'] += 1

                    # Horizontal axis
                    # Right
                    if p[2]+l < 10:
                        x = board[p[0], p[1], p[2]:p[2]+l] == " "
                        for i in x:
                            if i == True:
                                c['E'] += 1
                    # Left
                    if p[2]-l >= 0:
                        x = board[p[0], p[1], p[2]:p[2]-l:-1] == " "
                        for i in x:
                            if i == True:
                                c['W'] += 1
                    
                    # Here compares which direction is equal to the length to be listed in "d"
                    d = [k for k, v in c.items() if v == l]

                    return d
            else:
                raise ValueError

        except IndexError as ie:
            print(f"""{ie}
            REMEMBER: your board is shape {board.shape}.
                -The board indexing stars by 0, so at the ninth index is a total of 10 indexes.
                -Your board must have a shape of (2, 10, 10).
                -The position must belong within the board bonds.
            """)
        except ValueError as ve:
            print(f"""The length must be an int number equal or higher than 0 and smaller than 9.""")

    def rand_direction(board, position=tuple, length=int):
        """
        With the possible directions extracted from the function 'direction',
        this function chooses a random direction from the output (list).

        Parameters:
            -board: type array. A 3 dimensional matrix
            -position: type tuple. The start boat coordinates.
            -length: boat length as integer.
        
        Return:
            A string.
        """
        directions = BattleShip.direction(board, position, length)
        d = np.random.choice(directions)
        return d

    def boat_placer(board, position=tuple, length=int, direction=str):
        """
        Rewrites the array board with the placed boat.

        Parameters:
            -board: type array. A 3 dimensional matrix
            -position: type tuple. The start boat coordinates.
            -length: boat length as integer.
            -direction: string type. Direction were the boat will be placed in the matrix coordinates.
        
        Return:
            It doesn't return anything. Rewrites the current array with 'O'
        """
        d = direction
        p = position
        l = length

        # Indexing backwards in negative axis never lands in 0, always in -1
        # But the array is indexed from 0 to 9 in both axis
        # So for 'N' and 'W' directions we must slice rather in positive
        if d == "N":
            f_p = (p[0], p[1]+1-l, p[2])
            board[p[0], p[1]:p[1]-l:-1, p[2]] = "O"
        elif d == "S":
            board[p[0], p[1]:p[1]+l, p[2]] = "O"
        elif d == "W":
            f_p = (p[0], p[1], p[2]+1-l)
            board[p[0], p[1], f_p[2]:p[2]+1] = "O"
        else: # d == "E":
            board[p[0], p[1], p[2]:p[2]+l] = "O"
