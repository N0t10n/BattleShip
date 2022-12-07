from random import randint

def rand_p(board:list, level=0) -> tuple:
        """
        Calculates a random point in the array.

        Args
            -board: Two-dimensional array like.
            -level: Dimension of the array (board).
        
        Returns
            A random point from the dimension of the array.
        """
        point = (level,) + tuple(randint((board.shape[1], board.shape[2])))

        if board[point] == " ":
            return point
        else:
            return rand_p(board)