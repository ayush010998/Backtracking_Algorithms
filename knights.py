#knights-tour problem

# problem-statement-> Problem Statement:
#Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must visit each square exactly once. Print the order of each cell in which they are visited.

n=8
def isSafe(x,y,board):
    if(x>=0  and y>=0 and x<n and y<n and board[x][y]==-1):
        return True
    return False
def printSolutions(n,board):
    for i in range(n):
        for j in range(n):
            print(board[i][j])
            

def solvekt(n):
    board=[[-1 for i in range(n)] for i in range(n)]            
    move_x=[2,1,-1,-2,-2,-1,1,2]
    move_y=[1,2,2,1,-1,-2,-2,-1]
    board[0][0]=0
    pos=1
    if(not solvektutil(n,board,0,0,move_x,move_y,pos)):
        print("solution does not exsisits")
    else:
        printSolutions(n,board)

def solvektutil(n,board,curr_x,curr_y,move_x,move_y,pos):
    for i in range(8):
        new_x=curr_x+move_x[i]
        new_y=curr_y+move_y[i]
        if isSafe(new_x,new_y,board):
            board[new_x][new_y]=pos
            if(solvektutil(n,board,new_x,new_y,move_x,move_y,pos)):
                return True
            board[new_x][new_y]=-1
    return False


if __name__ == "__main__":
      
    # Function Call
    solvekt(n)
