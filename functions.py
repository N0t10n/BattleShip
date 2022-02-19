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
            -board: type array. A 3 dimensional position.
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

        