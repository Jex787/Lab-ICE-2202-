#include <iostream>
#include <vector>
using namespace std;

void knapsack(vector<int> &P, vector<int> &W, int C, int n)
{
    vector<vector<int>> dp(n + 1, vector<int>(C + 1, 0));
    vector<vector<bool>> selected(n + 1, vector<bool>(C + 1, false));

    for (int i = 1; i <= n; ++i)
    {
        for (int w = 1; w <= C; ++w)
        {
            if (W[i - 1] <= w)
            {
                dp[i][w] = max(P[i - 1] + dp[i - 1][w - W[i - 1]], dp[i - 1][w]);
                if (P[i - 1] + dp[i - 1][w - W[i - 1]] > dp[i - 1][w])
                {
                    selected[i][w] = true;
                }
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << "Maximum profit: " << dp[n][C] << endl;
    cout << "Selected items: ";
    int i = n, j = C;
    while (i > 0 && j > 0)
    {
        if (selected[i][j])
        {
            cout << i << " ";
            j -= W[i - 1];
        }
        --i;
    }
    cout << endl;
}

int main()
{
    int n, C;
    cout << "Enter the number of items: ";
    cin >> n;
    cout << "Enter the knapsack capacity: ";
    cin >> C;

    vector<int> P(n), W(n);
    cout << "Enter the profits of items: ";
    for (int i = 0; i < n; ++i)
    {
        cin >> P[i];
    }
    cout << "Enter the weights of items: ";
    for (int i = 0; i < n; ++i)
    {
        cin >> W[i];
    }

    knapsack(P, W, C, n);

    return 0;
}
