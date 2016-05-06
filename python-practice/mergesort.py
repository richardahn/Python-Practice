'''
Mergesort Implementation
'''
import random

def merge(left, right):
    '''
    [Merges two sorted lists into a new sorted one]

    Arguments:
    -   left: sorted list of comparable items
    -   right: sorted list of comparable items
    Returns:
    -   list: the merged sorted list
    '''
    # Empty lists are false, filled lists are true
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

def mergesort(list):
    '''
    [Sorts a list using mergesort]

    Arguments:
    -   list: a list of comparable items
    Returns:
    -   list: the sorted list
    Raises:
    -   Nothing
    '''
    if len(list) < 2:
        return list

    middle = len(list) // 2         # Note the usage of // for truncation
    left = mergesort(list[:middle])     # sort the left half in range [0, mid)
    right = mergesort(list[middle:])    # sort the right half in range [mid, len)
    return merge(left, right)


def print_list(list):
    '''
    [Prints a list]

    Arguments:
    -   list: a list of things to print
    Returns:
    -   None
    Raises:
    -   Nothing
    '''
    for x in list:
        print(x, end=" ")
    print()

def gen_rand_list(size, left, right):
    '''
    [Returns a randomly generated list of a given size with numbers
    between left and right]

    Arguments:
    -   size: size of the list
    -   left: lower bound of random gen
    -   right: upper bound of random gen
    Returns:
    -   list: a randomly generated list
    Raises:
    -   Nothing
    '''
    list = []
    for x in range(0, size):
        list.append(random.randint(left, right))
    return list

if __name__ == '__main__':
    print('Testing mergesort on numbers')
    list = gen_rand_list(10, 0, 1000)
    print_list(list)
    list = mergesort(list)
    print_list(list)
    print()
    print('Testing mergesort to sort by last name then first name')
