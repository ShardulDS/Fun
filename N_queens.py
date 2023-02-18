import numpy as np
n = 4
 
def isSafe(board, row, col):
 
    # Check this row on left side
    for i in range(col):
        if (board[row][i]):
            return False
 
    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
 
    # Check lower diagonal on left side
    i = row
    j = col
    while j >= 0 and i < n:
        if(board[i][j]):
            return False
        i = i + 1
        j = j - 1
 
    return True
 
 
def solveNQUtil(board, col, result, n):
    if (col == n):
        v = []
        for i in board:
          for j in range(len(i)):
            if i[j] == 1:
              v.append(j+1)
        result.append(v)
        return True
 

    res = False
    for i in range(n):
        if (isSafe(board, i, col)):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1, result, n) or res
            board[i][col] = 0  # BACKTRACK
    return res
 
result = []
board = [[0 for j in range(n)] for i in range(n)]
solveNQUtil(board,0,result,n)
res = []
k = 0
for i in range(len(result)):
    res.append(['']*n)
    for j in range(n):
        for k in range(n):
            if result[i][j]!=k+1:
                res[i][k] += '.'
            else:
                res[i][k] += 'Q'