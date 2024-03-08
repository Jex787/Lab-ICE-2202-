#include <iostream>
#include <vector>
using namespace std;

void print_solution(vector<vector<int>> &board, int n)
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

bool is_safe(vector<vector<int>> &board, int row, int col, int n)
{
    // Check left side of the row
    for (int i = 0; i < col; ++i)
    {
        if (board[row][i] == 1)
        {
            return false;
        }
    }

    // Check upper diagonal on left side
    for (int i = row, j = col; i >= 0 && j >= 0; --i, --j)
    {
        if (board[i][j] == 1)
        {
            return false;
        }
    }

    // Check lower diagonal on left side
    for (int i = row, j = col; i < n && j >= 0; ++i, --j)
    {
        if (board[i][j] == 1)
        {
            return false;
        }
    }

    return true;
}

bool solve_n_queens_util(vector<vector<int>> &board, int col, int n)
{
    if (col >= n)
    {
        print_solution(board, n);
        return true;
    }

    bool res = false;
    for (int i = 0; i < n; ++i)
    {
        if (is_safe(board, i, col, n))
        {
            board[i][col] = 1;

            res = solve_n_queens_util(board, col + 1, n) || res;

            board[i][col] = 0; // Backtrack
        }
    }

    return res;
}

void solve_n_queens(int n)
{
    vector<vector<int>> board(n, vector<int>(n, 0));

    if (!solve_n_queens_util(board, 0, n))
    {
        cout << "Solution does not exist." << endl;
    }
}

int main()
{
    int n;
    cout << "Enter the number of queens (N): ";
    cin >> n;

    solve_n_queens(n);

    return 0;
}
