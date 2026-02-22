def boardprint(board):
    for row in board:
        print(row)
def empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c]=='-':
                return r,c
    return None
def isvalid(board,row,col,num):
    for j in range(9):
        if board[row][j]==num:
            return False
    for i in range(9):
        if board[i][col]==num:
            return False
    start_row = (row//3)*3
    start_col = (col//3)*3
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if board[i][j]==num:
                return False
    return True
\
def body(board):
    emptybox = empty(board)
    if not emptybox:
        return True
    row,col = emptybox
    for num in '123456789':
        if isvalid(board,row,col,num):
            board[row][col]=num
            if body(board):
                return True
            board[row][col]='-'
    return False 