# Data Structures II
# Gregory Walsh Z# Z00265853
# Programming Assignment 1
# Date Started 2-2-18
# testsorts.py

# Need to import random (for random list) and sorts (for the sorting)
import random
import sorts


def random_list(length, a=0, b=100):
    """
    random_list creates a random list using the 3 parameters:
    'length' is the length of the list.
    'a' is the minimum of the numbers values in the list
    'b' is the maximum of the numbers values in the list
    default values for a = 0 & b = 100
    eg. (10, 0, 50) will create a list size of 10 with numbers
    ranging from 0-50
    """
    # Create an empty list to store data
    list = []
    # For loop for the length range to get random number and store in a list
    for num in range(length):
        number = random.randint(a, b)
        list.append(number)
    return list


def is_sorted(check):
    """
    is_sorted will test if a list is sorted
    parameters:
    'check' List to be checked
    will return a Boolean value
    """
    if sorted(check) == check:
        return True
    else:
        return False


def test_insertion_sort(shortlist, longlist, numlist):
    """
    test_insertion_sort will test if the insertion sort function sorted the given list
    parameters:
    'shortlist' The length of the shortest list to test
    'longlist' The length of the longest list to test
    'numlist' The number of lists of each length to test
    eg. test_insertion_sort(5, 10, 9) will test insertion sort of a list size of 5 through 10 and will test 9 lists of each
    """
    for j in range(shortlist, longlist + 1):
        print("Testing Length", j)
        for k in range(numlist):
            print("List Number  ", k + 1)
            createlist = random_list(j)
            print("List Unsorted", createlist)
            sorts.insertion_sort(createlist)
            print("List Sorted  ", createlist)

            if not is_sorted(createlist):
                assert type(error), "Failed to sort"
                print("Error Length", j)
            else:
                print("Success!")


def test_merge_sort(shortlist, longlist, numlist):
    """
    test_merge_sort will test if the merge sort function sorted the given list
    parameters:
    'shortlist' The length of the shortest list to test
    'longlist' The length of the longest list to test
    'numlist' The number of lists of each length to test
    eg. test_merge_sort(5, 10, 9) will test merge sort of a list size of 5 through 10 and will test
    9 lists of each
    """
    for j in range(shortlist, longlist + 1):
        print("Testing Length", j)
        for k in range(numlist):
            print("List Number  ", k + 1)
            createlist = random_list(j)
            print("List Unsorted", createlist)
            sorts.merge_sort(createlist)
            print("List Sorted  ", createlist)

            if not is_sorted(createlist):
                assert type(error), "Failed to sort"
                print("Error Length", j)
            else:
                print("Success!")


# DEBUG BELOW PLEASE IGNORE
#------------------------------------------
# test = random_list(10)
# print(test)
# sorts.merge_sort(test)
# print(test)
# print(is_sorted(test))
# test_merge_sort(1, 3, 2)
# test_insertion_sort(1, 3, 2)
