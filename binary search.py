def binary_search(arr, x):
    """
    Perform binary search to find the index of element x in sorted array arr.

    Parameters:
    - arr: List of sorted elements
    - x: Element to search for

    Returns:
    - int: Index of element x if found, else -1
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 7
print(binary_search(arr, x))  # Expected output: 6
