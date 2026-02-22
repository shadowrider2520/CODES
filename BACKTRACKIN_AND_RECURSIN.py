"""
def n_queens(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(".")
        board.append(row)
    
    solutions = []

    def is_safe(row,col):

        for i in range(row):
            if board[i][col]=="Q":
                return False
        i = row-1
        j = col-1
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i-=1
            j-=1
        i = row-1
        j = col+1
        while i>=0 and j<n:
            if board[i][j]=="Q":
                return False
            i-=1
            j+=1
        return True


    def place_queens(row):
        if row==n:
            solution = []
            for r in board:
                solution.append("".join(r))
            solutions.append(solution)
            return 
        for col in range(n):
            if is_safe(row,col):
                board[row][col]="Q"
                place_queens(row+1)
                board[row][col]="."

    place_queens(0)
    return solutions"""

"""def paranthesis(n):
    result = []
    def dfs(left,right,current):
        if left==n and right==n:
            result.append(current)
            return 
        if left>n:
            dfs(left+1,right,current+"(")
        if right<left:
            dfs(left,right+1,current+")")
    dfs(0,0,"")
    return result"""

"""def pathgen(m,n):
    result = []
    def dfs(r,c,path):
        rpos = m-1
        cpos = n-1
        if r==rpos and c==cpos:
            result.append(path)
            return
        if r<rpos:
            dfs(r+1,c,path + "D")
        if c<cpos:
            dfs(r,c+1,path+ "R")
    dfs(0,0,"")
    return result

print(pathgen(2,2))"""

"""def string_powerset(s):
    result = []
    def dfs(index,current):
        if index==len(s):
            result.append(current)
            return
        dfs(index+1,current)
        dfs(index+1,current+s[index])
    dfs(0,'')
    return result"""

"""def binarygen(n):
    result = []
    def dfs(current):
        if len(current)==n:
            result.append(current)
            return
        dfs(current+"1")
        dfs(current+"0")
    dfs("")
    return result"""