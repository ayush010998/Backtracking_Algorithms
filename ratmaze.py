"""
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down. 

In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. Note that this is a simple version of the typical Maze problem. For example, a more complex version can be that the rat can move in 4 directions and a more complex version can be with a limited number of moves.

"""


n=4

def isvalid(n,maze,x,y,res):
    if x>=0 and y>=0 and x<n and y<n and maze[x][y]==1 and res[x][y]==0:
        return True
    return False

def ratMaze(n,maze,move_x,move_y,x,y,res):
    if x==n-1 and y==n-1:
        return True
    for i in range(4):
        x_new=x+move_x[i]
        y_new=y+move_y[i]
        if isvalid(n,maze,x_new,y_new,res):
            res[x_new][y_new]=1
            if ratMaze(n,maze,move_x,move_y,x_new,y_new,res):
                return True
            res[x_new][y_new]=0
    return False


def solveMaze(maze):
    # Creating a 4 * 4 2-D list
    res = [[0 for i in range(n)] for i in range(n)]
    res[0][0] = 1
  
    # x matrix for each direction
    move_x = [-1, 1, 0, 0]
  
    # y matrix for each direction
    move_y = [0, 0, -1, 1]
  
    if ratMaze(n, maze, move_x, move_y, 0, 0, res):
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
    else:
        print('Solution does  not exist')
  
  
# Driver program to test above function
if __name__ == "__main__":
    # Initialising the maze
    maze = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [0, 1, 0, 0],
             [1, 1, 1, 1]]
  
    solveMaze(maze)

