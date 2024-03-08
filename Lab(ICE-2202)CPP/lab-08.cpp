#include <iostream>
#include <vector>
using namespace std;

bool subset_sum(vector<int> &S, int d)
{
    int n = S.size();
    vector<vector<bool>> dp(n + 1, vector<bool>(d + 1, false));

    // Initialize the first column to true (subset sum 0 can always be achieved)
    for (int i = 0; i <= n; ++i)
    {
        dp[i][0] = true;
    }

    // Fill the dp array
    for (int i = 1; i <= n; ++i)
    {
        for (int j = 1; j <= d; ++j)
        {
            if (j < S[i - 1])
            {
                dp[i][j] = dp[i - 1][j];
            }
            else
            {
                dp[i][j] = dp[i - 1][j] || dp[i - 1][j - S[i - 1]];
            }
        }
    }

    return dp[n][d];
}

int main()
{
    int n;
    cout << "Enter the number of elements in the set: ";
    cin >> n;

    vector<int> S(n);
    cout << "Enter the elements of the set: ";
    for (int i = 0; i < n; ++i)
    {
        cin >> S[i];
    }

    int d;
    cout << "Enter the target sum: ";
    cin >> d;

    if (subset_sum(S, d))
    {
        cout << "Subset with sum " << d << " exists." << endl;
    }
    else
    {
        cout << "No subset with sum " << d << " exists." << endl;
    }

    return 0;
}
