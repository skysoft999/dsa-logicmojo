"""
Qn: Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in O(n) time complexity and O(1) Space complexity with only one traversal Asked in : Amazon, Adobe , Walmart

Array consist of only 0's, 1's and 2's. Write an algorithm to sort  this array in O(n) time complexity and O(1) Space complexity with only one traversal



Algo:

    1. pointer> [0]-> low,mid [n] -> high

    2. if aray[mid] == 2 ? => swap(array[mid], array[high]) & high --

    3. if array[mid] == 0 ? =>swap(array[mid], array[low]) & low++ mid++

    4. if array[mid] == 1 ? => No Swap & mid ++

"""


def array_seg(array):
    """ my solution array seggregation logic for an array with elements 0, 1, 2"""
    size = len(array)
    low = mid = 0
    high = size - 1

    while mid <= high:
        temp = 0
        if array[mid] == 0:
            temp = array[mid]
            array[mid] = array[low]
            array[low] = temp
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            temp = array[mid] 
            array[mid] = array[high]
            array[high] = temp
            high -= 1
        else:
            print("invald array")
            break


def swap(array, i, j):
    """swap-logic logic mojo solution """
 
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def sort_0_1_2(array):
    """ logic mojo solution  """
 
    low = mid = 0
    high = len(array) - 1
 
    while mid <= high:
        if array[mid] == 0:
            swap(array, low, mid)
            low = low + 1
            mid = mid + 1
        elif array[mid] == 2:
            swap(array, mid, high)
            high = high - 1
        else:
            mid = mid + 1


def array_seg_recursive(array, low, mid, high):
    """recursive solution mine """
    if mid > high:
        return
    else:
        if array[mid] == 0:
            temp = array[mid]
            array[mid] = array[low]
            array[low] = temp
            low += 1
            mid += 1
            return array_seg_recursive(array, low, mid, high)
        elif array[mid] == 1:
            mid += 1
            return array_seg_recursive(array, low, mid, high)
        else:
            temp = array[mid] 
            array[mid] = array[high]
            array[high] = temp
            high -= 1
            return array_seg_recursive(array, low, mid, high)            


if __name__ == "__main__":
    # array = [0, 1, 2, 0, 1, 2]
    array = [2, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    # array_seg(array)
    array_seg_recursive(array, 0, 0, len(array)-1)
    print(f"Seggregated array result: {array}")
