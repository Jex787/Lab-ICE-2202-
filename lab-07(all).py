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


def solve_n_queens_util(board, col, n, result):
    # If all queens are placed then return true
    if col >= n:
        result.append([row[:] for row in board])
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            res = solve_n_queens_util(board, col + 1, n, result) or res

            # If placing queen in board[i][col] doesn't lead to a solution then
            # remove queen from board[i][col]
            board[i][col] = 0

    # Return false if no queen can be placed in this column
    return res


def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = []

    if not solve_n_queens_util(board, 0, n, result):
        print("No solution exists.")
        return

    # Print all possible solutions
    for sol in result:
        for row in sol:
            print(" ".join(map(str, row)))
        print()


if __name__ == "__main__":
    n = int(input("Enter the value of N: "))
    solve_n_queens(n)
