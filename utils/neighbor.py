def neighbor(board:list, position:tuple, level:int) -> dict:
        """
        Find all possible free positions arround the given cell (position).

        Args
            -board: Two-dimensional array like.
            -position: Pivot point on the board.
            -level: Dimension of the array (board).

        Return
            A dictionary containning in True the positions where there's a boat cell (O)
            plced in the board and False the positions where is a water cell (" ").
        """

        p = position
        pos_dict = {True: 0, False: 0}

        def write_on_board(board:list, position:tuple):
            global pos_dict

            if board[position] == " ":
                pos_dict[False].append(position)

            elif board[position] == 'O':
                pos_dict[True].append(position)

            else:
                pass

        # Above
        if p[1] > 0:
            pos = (level,) + (p[1]-1,) + (p[2],)
            write_on_board(board, pos)

        # Below
        if p[1] < 9:
            pos = (level,) + (p[1]+1,) + (p[2],)
            write_on_board(board, pos)

        # Left
        if p[2] > 0:
            pos = (level,) + (p[1],) + (p[2]-1,)
            write_on_board(board, pos)

        # Right
        if p[2] < 9:
            pos = (level,) + (p[1],) + (p[2]+1,)
            write_on_board(board, pos)

        # Above-right
        if p[1] > 0 and p[2] < 9:
            pos = (level,) + (p[1]-1,) + (p[2]+1,)
            write_on_board(board, pos)

        # Above-left
        if p[1] > 0 and p[2] > 0:
            pos = (level,) + (p[1]-1,) + (p[2]-1,)
            write_on_board(board, pos)

        # Below-right
        if p[1] < 9 and p[2] < 9:
            pos = (level,) + (p[1]+1,) + (p[2]+1,)
            write_on_board(board, pos)

        # Below-left
        if p[1] < 9 and p[2] > 0:
            pos = (level,) + (p[1]+1,) + (p[2]-1,)
            write_on_board(board, pos)

        return pos_dict