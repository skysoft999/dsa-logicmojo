"""
Qn: Maximum Value in an array of Increasing and Decreasing using Binary Search

---
One array of integers is given as an input ,which is initially 
increasing and then decreasing or it can be only increasing or decreasing , 
you need to find the maximum value 
in the array in O(Log n) Time complexity and O(1) 
Space Complexity Asked in : [Amazon, Microsoft, Uber]

---

* all the elements are consist of 3 properties:

1. Left us less & right is more 

2. Left is More & Right is Less

3. Left is Less & Right is less (possible answer)


>> whenever problem links with array search think about binary search 
which can solve by O(logn)

>> eg: [6,9,15,25,35,50,41,29,23,8]
    
    * pointer @ 50 = array[mid] >array[mid-1] & array[mid] > array[mid+1] : mid index conatains value max
    * pointer @35 = array[mid] > array[mid-1] & array[mid] < array[mid+1]: we can skip Left part max value can occupy right: make start=mid+1
    * all other case = we can skip right part max value can occupy left: make end=mid-1


"""

import unittest


def find_max_val(array, start, end):
    """ my try """
    if start == end:
        return array[start]

    if end == start + 1:
        if array[start] > array[end]:
            return array[start]
        else:
            return array[end]
    mid = (start + end) // 2

    if array[mid] > array[mid + 1] and array[mid] < array[mid - 1]:
        return find_max_val(array, start, mid - 1)
    if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
        return array[mid]
    else:
        return find_max_val(array, mid + 1, end)


if __name__ == "__main__":
    array = [6, 9, 15, 25, 35, 50, 41, 29, 23, 8]
    res = find_max_val(array, 0, len(array) - 1)
    print(f"Maximum Value is {res}")


# Logic Mojo Soln


def findMaxValue(array, start, end):
    # Only one element is present in array[start..end]
    if start == end:
        return array[start]
    # If there are two elements and first is greater then the first element is maximum */
    if end == start + 1:
        if array[start] >= array[end]:
            return array[start]
        else:
            # If there are two elements and second is greater then the second element is maximum
            return array[end]

    mid = (start + end) // 2  # low + (high - low)/2
    # If we reach a point where arr[mid] is greater than both of its adjacent elements array[mid-1] and array[mid+1], then array[mid] is the maximum element
    if array[mid] > array[mid + 1] and array[mid] > array[mid - 1]:
        return array[mid]
    # If array[mid] is greater than the next element and smaller than the previous element then maximum lies on left side of mid */
    if array[mid] > array[mid + 1] and array[mid] < array[mid - 1]:
        return findMaxValue(array, start, mid - 1)
    else:  # when array[mid] is greater than array[mid-1] and smaller than array[mid+1]
        return findMaxValue(array, mid + 1, end)


class Test(unittest.TestCase):
    def test_findMaxValue_1(self):
        actual = findMaxValue([3, 5, 15, 50, 11, 10, 8, 6], 0, 7)
        expected = 50
        self.assertEqual(actual, expected)

    def test_findMaxValue_2(self):
        actual = findMaxValue([10, 20, 30, 40, 50], 0, 4)
        expected = 50
        self.assertEqual(actual, expected)

    def test_findMaxValue_3(self):
        actual = findMaxValue(
            [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1], 0, 10)
        expected = 500
        self.assertEqual(actual, expected)

    def test_findMaxValue_4(self):
        actual = findMaxValue([120, 100, 80, 20, 0], 0, 4)
        expected = 120
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
