def binary_search(arr, target):
    """
    Perform binary search to find the target element in the sorted array.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Input section to take a sorted list and the target element from the user
arr = list(map(int, input("Enter a sorted list of numbers separated by space: ").split()))
target = int(input("Enter the element to search for: "))

# Perform binary search
index = binary_search(arr, target)

# Output the result
if index != -1:
    print("Element", target, "found at index:", index)
else:
    print("Element", target, "not found in the list.")
