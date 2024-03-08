def subset_sum_recursive(S, n, d):
    # Base cases
    if d == 0:
        return True
    if n == 0:
        return False
    
    # If last element is greater than d, then ignore it
    if S[n - 1] > d:
        return subset_sum_recursive(S, n - 1, d)
    
    # Check if sum can be obtained by including or excluding the last element
    return subset_sum_recursive(S, n - 1, d) or subset_sum_recursive(S, n - 1, d - S[n - 1])


def subset_sum(S, d):
    n = len(S)
    return subset_sum_recursive(S, n, d)


# Input section to take the value of S and d from the user
S = list(map(int, input("Enter the elements of the set S separated by space: ").split()))
d = int(input("Enter the target sum d: "))

if subset_sum(S, d):
    print("Subset with sum", d, "exists.")
else:
    print("No subset with sum", d, "exists.")
