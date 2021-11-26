"""
Linear time approach to solve jump game problem

* PS: This can be also implement using backtracking.


qn:

Asked In: AdobeIntuit
You have an array of non-negative integers,you are initially
positioned at the first index of the array.
Each element in the array represents your maximum jump length
at that position.Determine if you are able to reach
the last index in O(n) Time complexity and O(1)
Space Complexity Asked in: Adobe, Intuit


---
Input 1:
A = [2,3,1,1,4]
Input 2:
A = [3,2,1,0,4]

---
Output 1:
2
Explanation 1:
Index 0 -> Index 2 -> Index 4

---

Output 2:
0
Explanation 2:
There is no possible path to reach the last index return -1

----

1. get array, arraysize
2. a = array[0], b= array[0], jump = 1
    * i range(1,n) 1<-----> n-1
3. a-- , b--

4. array[i] > b?
    * b= array[i]

5. a == 0?
    * jump ++
    * a = b


"""


def minJumpsToEnd(num, n):
    # The number of jumps needed to reach the starting index is 0
    if (n <= 1):
        return 0

    # Return -1 if not possible to jump
    if (num[0] == 0):
        return -1

    # stores all time the maximal reachable index in the num array
    a = num[0]
    # stores the amount of steps we can still take
    b = num[0]
    # stores the amount of jumps
    # necessary to reach that maximal reachable position
    jump = 1

    for i in range(1, n):
        # Check if we have reached the end of the array
        if (i == n - 1):
            return jump

        # we use a ,b to get to the current index
        b -= 1
        a -= 1

        if (num[i] > b):
            b = num[i]
        # If no further bs left
        if (a == 0):
            # we must have used a jump
            jump += 1
            a = b
        # Exception scenario when we failed to reach the end, simplay return -1
        if (b == 0):
            return -1
    return jump


# def minJumps(arr, n):
#     """ try2 for minJumps """
#     # The number of jumps needed to reach the starting index is 0
#     if (n <= 1):
#         return 0

#     # Return -1 if not possible to jump
#     if (arr[0] == 0):
#         return -1

#     # initialization
#     # stores all time the maximal reachable index in the array
#     maxReach = arr[0]
#     # stores the amount of steps we can still take
#     step = arr[0]
#     # stores the amount of jumps necessary to reach that maximal reachable position
#     jump = 1

#     # Start traversing array

#     for i in range(1, n):
#         # Check if we have reached the end of the array
#         if (i == n-1):
#             return jump

#         # updating maxReach
#         maxReach = max(maxReach, i + arr[i])

#         # we use a step to get to the current index
#         step -= 1

#         # If no further steps left
#         if (step == 0):
#             # we must have used a jump
#             jump += 1

#             # Check if the current index / position or lesser index
#             # is the maximum reach point from the previous indexes
#             if(i >= maxReach):
#                 return -1

#             # re-initialize the steps to the amount
#             # of steps to reach maxReach from position i.
#             step = maxReach - i
#     return -1


if __name__ == "__main__":
    array = [1, 1, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    res = minJumpsToEnd(array, len(array))
    print(f"minimum jump required is: {res}")
