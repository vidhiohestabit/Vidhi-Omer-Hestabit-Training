def linear_search(arr, target):
    """
    Searches for the target element in the given array.

    Args:
        arr (list): The list to search in.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, -1 otherwise.
    """
    # Loop through each element in the array
    for i in range(len(arr)):
        # Print the current index for debugging
        print(f"Checking element at index {i}")
        
        # Check if the current element matches the target
        if arr[i] == target:
            # If a match is found, return the index
            print(f"Target {target} found at index {i}")
            return i
    
    # If no match is found after looping through the entire array, return -1
    print(f"Target {target} not found in the list")
    return -1

# Example usage:
arr = [3, 6, 1, 8, 2, 4, 8, 10]
target = 8
index = linear_search(arr, target)

if index != -1:
    print(f"The target {target} is found at index {index}.")
else:
    print(f"The target {target} is not found in the list.")