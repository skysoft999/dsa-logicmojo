
import unittest


class Test(unittest.TestCase):
    def test_binarySearch_1(self):
        actual = binary_search_recur([2, 5, 6, 8, 9, 10], 0, 5, 5)
        expected = 1
        self.assertEqual(actual, expected)

    def test_binarySearch_2(self):
        actual = binary_search_recur(
            [16, 19, 20, 23, 45, 56, 78, 90, 96, 100], 0, 9, 45)
        expected = 4
        self.assertEqual(actual, expected)

    def test_binarySearch_3(self):
        actual = binary_search_recur([2, 3, 4, 10, 40], 0, 4, 10)
        expected = 3
        self.assertEqual(actual, expected)

    def test_binarySearch_4(self):
        actual = binary_search_recur([3, 4, 5, 6, 7, 8, 9], 0, 6, 4)
        expected = 1
        self.assertEqual(actual, expected)


def binary_search_recur(array, left, right, elem):

    if left > right:
        return -1

    mid = (left + right) // 2

    if elem == array[mid]:
        return mid
    elif elem < array[mid]:
        return binary_search_recur(array, left, mid - 1, elem)
    else:
        return binary_search_recur(array, mid + 1, right, elem)


def binary_search_iter(array, key):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if key > array[mid]:
            low = mid + 1

        elif key < array[mid]:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    array = [16, 19, 20, 23, 45, 56, 78, 90, 96, 100]
    to_find = 45
    # iterative binary search
    res = binary_search_iter(array, to_find)
    if res and res != -1:
        print(f"found element on {res} index!")
    else:
        print("element not found")
    # unit test on recursive way
    unittest.main(verbosity=2)
