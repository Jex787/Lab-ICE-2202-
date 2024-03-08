def is_safe(board, row, col, n):
    # Check left side of the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n):
    # If all queens are placed, return true
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then backtrack
            board[i][col] = 0

    # If queen can't be placed in any row in this column col, then return false
    return False


def solve_n_queens(n):
    # Initialize the board with zeros
    board = [[0] * n for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return False

    # Print the solution
    print_solution(board)
    return True


def print_solution(board):
    for row in board:
        print(" ".join(map(str, row)))


# Input section to take the value of n from the user
n = int(input("Enter the value of n: "))
solve_n_queens(n)

