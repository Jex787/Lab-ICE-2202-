def linear_search(arr, target):
    """
    Perform linear search to find the target element in the array.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Input section to take a list and the target element from the user
arr = list(map(int, input("Enter a list of numbers separated by space: ").split()))
target = int(input("Enter the element to search for: "))

# Perform linear search
index = linear_search(arr, target)

# Output the result
if index != -1:
    print("Element", target, "found at index:", index)
else:
    print("Element", target, "not found in the list.")
