#problem statements :-  he N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other. For example, the following is a solution for the 4 Queen problem.

"""
Time Complexity: O(N*NCN)
Auxiliary Space: O(N2)

Algorithm for N queen problem:
Following is the backtracking algorithm for solving the N-Queen problem

Initialize an empty chessboard of size NxN.
Start with the leftmost column and place a queen in the first row of that column.
Move to the next column and place a queen in the first row of that column.
Repeat step 3 until either all N queens have been placed or it is impossible to place a queen in the current column without violating the rules of the problem.
If all N queens have been placed, print the solution.
If it is not possible to place a queen in the current column without violating the rules of the problem, backtrack to the previous column.
Remove the queen from the previous column and move it down one row.
Repeat steps 4-7 until all possible configurations have been tried.



""" 


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        grid = [['.' for _ in range(n)] for _ in range(n)]
        solved = self.helper(n, 0, grid)
        if solved:
            return ["".join(item) for item in grid]
        else:
            return None

    def helper(self, n, row, grid):
        if n == row:
            return True
        for col in range(n):
            if self.is_safe(row, col, grid):
                grid[row][col] = 'Q'
                if self.helper(n, row + 1, grid):
                    return True
                else:
                    grid[row][col] = '.'
        return False

    def is_safe(self, row, col, board):
        for i in range(len(board)):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
        i = 0
        while row - i >= 0 and col - i >= 0:
            if board[row - i][col - i] == 'Q':
                return False
            i += 1
        i = 0
        while row + i < len(board) and col + i < len(board):
            if board[row + i][col - i] == 'Q':
                return False
            i += 1
        i = 1
        while row + i < len(board) and col - i >= 0:
            if board[row + i][col - i] == 'Q':
                return False
            i += 1
        i = 1
        while row - i >= 0 and col + i < len(board):
            if board[row - i][col + i] == 'Q':
                return False
            i += 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(8))