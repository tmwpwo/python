

b = [[8,3,0,6,0,0,0,5,7], 
    [7,4,0,8,1,0,0,9,6], 
    [1,0,0,0,0,7,0,8,0], 
    [4,0,9,5,8,0,7,6,0], 
    [3,0,0,2,6,0,0,0,0], 
    [5,0,0,0,7,3,0,2,0], 
    [0,0,4,1,0,5,0,0,2], 
    [0,1,3,0,0,0,0,0,0], 
    [2,0,7,9,4,0,8,0,0]]

def findEmpty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0 :
                return row, col
    return None

def validation(board, num, row, col):

    for j in range(9):
        if board[row][j] == num:
            return False

    for i in range(9):
        if board[i][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True

def solving(board):
    empty = findEmpty(b)
    if empty:
        row, col = empty
    else:
        return True

    for j in range(1,10):
        if validation(b,j,row,col):
            b[row][col] = j

            if solving(b):
                return True
            
            b[row][col] = 0
    return False
    

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


solving(b)
print_board(b)




