def knapsack(P, W, C, n):
    # Initialize a 2D array to store the maximum profit for each subproblem
    dp = [[0] * (C + 1) for _ in range(n + 1)]

    # Fill the dp array using dynamic programming
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif W[i - 1] <= w:
                dp[i][w] = max(P[i - 1] + dp[i - 1][w - W[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Trace back to find the items included in the knapsack
    included_items = []
    i, w = n, C
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= W[i - 1]
        i -= 1

    # Return the maximum profit and the list of included items
    return dp[n][C], included_items


# Input section to take the values of P, W, C, and n from the user
P = list(map(int, input("Enter the profits of items separated by space: ").split()))
W = list(map(int, input("Enter the weights of items separated by space: ").split()))
C = int(input("Enter the knapsack capacity: "))
n = int(input("Enter the number of items: "))

max_profit, items_included = knapsack(P, W, C, n)
print("Maximum profit:", max_profit)
print("Items included:", items_included)
