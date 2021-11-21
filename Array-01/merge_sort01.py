import unittest


# Merge two sorted sub-lists arr[low .. mid] and arr[mid + 1 .. high]
def merge(arr, result, low, mid, high):

    k = low
    i = low
    j = mid + 1

    # While there are elements in the left and right runs
    while i <= mid and j <= high:

        if arr[i] <= arr[j]:
            result[k] = arr[i]
            k = k + 1
            i = i + 1
        else:
            result[k] = arr[j]
            k = k + 1
            j = j + 1

    # Copy remaining elements
    while i <= mid:
        result[k] = arr[i]
        k = k + 1
        i = i + 1

    # No need to copy the second half

    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        arr[i] = result[i]


# Sort list A [low..high] using auxiliary list aux
def mergeSort(arr, result, low, high):

    # Base case
    if high == low:  # if run size == 1
        return

    # find mid point
    mid = (low + high)//2

    # recursively split runs into two halves until run size == 1,
    # then merge them and return back up the call chain

    mergeSort(arr, result, low, mid)         # split / merge left  half
    mergeSort(arr, result, mid + 1, high)   # split / merge right half

    merge(arr, result, low, mid, high)     # merge the two half runs


def mergeSortFinal(arr, result, low, high):
    mergeSort(arr, result, low, high)
    return arr


# Function to check if arr is sorted in ascending order or not
def isSorted(arr):

    prev = arr[0]
    for i in range(1, len(arr)):
        if prev > arr[i]:
            print("MergeSort Fails!!")
            return False

        prev = arr[i]

    return True


class Test(unittest.TestCase):
    def test_mergeSort_1(self):
        arr = [8,4,3,12,25,6,13,10]
        result = arr.copy()
        actual = mergeSortFinal(arr, result, 0, len(arr) - 1)
        expected = [3, 4, 6, 8, 10, 12, 13, 25]
        self.assertEqual(actual, expected)

    def test_mergeSort_2(self):
        arr = [12, 11, 13, 5, 6, 7 ]
        result = arr.copy()
        actual = mergeSortFinal(arr, result, 0, len(arr) - 1)
        expected = [5, 6, 7, 11, 12, 13]
        self.assertEqual(actual, expected)

    def test_mergeSort_3(self):
        arr = [38, 27, 43, 3, 9, 82, 10]
        result = arr.copy()
        actual = mergeSortFinal(arr, result, 0, len(arr) - 1)
        expected = [3,9,10,27,38,43,82]
        self.assertEqual(actual, expected)

    def test_mergeSort_4(self):
        arr = [3,2,1,4]
        result = arr.copy()
        actual = mergeSortFinal(arr, result, 0, len(arr) - 1)
        expected = [1,2,3,4]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)