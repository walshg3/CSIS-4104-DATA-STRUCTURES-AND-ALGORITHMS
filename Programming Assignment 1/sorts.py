# Data Structures II
# Gregory Walsh Z# Z00265853
# Programming Assignment 1
# Date Started 2-2-18
# sorts.py


def insertion_sort(A):
    """
    insertion_sort will sort a given List using insertion sort. Parameters:
    'A' List to be sorte
    """
    for j in range(1, len(A)):
        key = A[j]
        # Inset A[j] into the sorted sequence
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key


def merge_sort(A):
    """
    Accepts a List and divides the List into 3 parameters:
    'A'
    '0'
    'len(A)-1'
    Primarily used for simplicity to the user (See merge for more detail)
    'A' is a List to be sorted.
    """
    # Take the list and divide it up to what is needed
    merge_sort_actual(A, 0, len(A) - 1)


def merge_sort_actual(A, begin, end):
    """
    merge_sort_actual will take the list from merge_sort and divide the list in half
    it will then merge the left and right side
    parameters:
    'A' List
    'begin' beginning of the List (index 0)
    'end' ending of the List(len(A))
    """

    # Determine if the List is greater than 1
    if begin < end:
        # Split the List in half
        middle = (begin + end) // 2
        # Merge Left and Right side
        # Left side
        merge_sort_actual(A, begin, middle)
        # Right side
        merge_sort_actual(A, middle + 1, end)
        # Merge function to join Left and Right side together
        merge(A, begin, middle, end)


def merge(A, begin, middle, end):
    """
    merge creates a Left and Right side of the List using the begin middle and end parameter.
    a For loop will then compare elements in Left and Right sides of the list to determine
    which element is greater and assign the element to the proper index of A (sorted)
    parameters:
    'A' List
    'begin' beginning of the List (index 0)
    'middle' middle of the List using modular division (mod division will handle even and odd sizes)
    'end' ending of the List(len(A))
    """
    # Assign Left and Right side of List
    Left = A[begin:middle + 1]
    Right = A[middle + 1:end + 1]
    # Append a number really big so program knows when to stop
    Left.append(99999999)
    Right.append(99999999)
    # Create Pointers i & j
    i = j = 0
    # For loop to compare Left and Right side of List
    for k in range(begin, end + 1):
        if Left[i] <= Right[j]:
            A[k] = Left[i]
            i += 1
        else:
            A[k] = Right[j]
            j += 1


# DEBUG BELOW PLEASE IGNORE
# --------------------------------------------------
# insertion_sort(A)
# A = [15, 5, 4, 18, 12, 19, 14, 8, 10, 20, 21]
# print("Before sort", A)
# merge_sort(A)
# print(A)
