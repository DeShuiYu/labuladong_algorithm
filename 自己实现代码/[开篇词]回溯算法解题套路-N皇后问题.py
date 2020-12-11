'''
for 选择 in 选择列表：
    # 做选择
    将该选择从选择列表移除
    路径.add(选择)
    backtrack(路径，选择列表)
    # 撤销选择
    路径.remove(选择)
    将该选择在加入选择列表
'''
import copy
res = []
def solveNQueens(n:int):
    board = [[0 for _ in range(n)] for _ in range(n)]
    backtrack(board,0)
    return res

def backtrack(board,row:int):
    if row == len(board):
        res.append(copy.deepcopy(board))
        return 
    for col in range(len(board[row])):
        if not isVaild(board,row,col):
            continue
        board[row][col] = 1
        backtrack(board,row+1)
        board[row][col] = 0
    
def isVaild(board,row,col):
    i,j = 0,0
    # 检查上面
    while i < row:
        if board[i][col] == 1:
            return False
        i+=1

    # 检查下面

    # 检查左上
    i,j = row - 1,col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 检查右上
    i ,j = row -1 , col+1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    

    return True
    

solveNQueens(8)
for index,arr in enumerate(res):
    print(f"第{index+1}种解法:")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                print("*",end=" ")
            elif arr[i][j] == 1:
                print("♛",end=" ")
        print()
    print()