def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    Args:
        arr (list): The input array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(arr)  # Get the length of the input array

    # Iterate from the second element to the end of the array
    for i in range(1, n):
        # Store the current element as 'key'
        key = arr[i]

        # Initialize a pointer 'j' to the previous element
        j = i - 1

        # Shift elements of arr[0..i-1], that are greater than 'key', to one position ahead of their current position
        while (j >= 0) and (key < arr[j]):
            arr[j + 1] = arr[j]  # Move the greater element one position ahead
            j = j - 1

        # Place the 'key' element at its correct position in the sorted sub-array
        arr[j + 1] = key

    return arr


# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)