# import sys
#
#
# def makePartition(array, left, right):
#     numToSort = array[left]
#     leftBeforeWork = left
#     left += 1
#     while left <= right:
#         areLeftAndRigthChanged = False
#         if array[left] < numToSort:
#             left += 1
#             areLeftAndRigthChanged = True
#         if array[right] > numToSort:
#             right -= 1
#             areLeftAndRigthChanged = True
#         if not areLeftAndRigthChanged:
#             array[left], array[right] = array[right], array[left]
#             right -= 1
#             left += 1
#     array[leftBeforeWork] = array[right]
#     array[right] = numToSort
#     # print(array,right)
#     return right
#
#
# def quickSort(array, left, right):
#     if right > left:
#         partition = makePartition(array, left, right)
#         quickSort(array, left, partition - 1)
#         quickSort(array, partition + 1, right)
#
#
# arr = []
# for _ in range(int(input())):
#     arr.append(int(input()))
# arr.append(sys.maxsize)
# quickSort(arr, 0, len(arr) - 1)
# for i in arr[0:len(arr) - 1]:
#     print(i)

import sys

arr = [0] * 10001
for i in range(int(sys.stdin.readline())):
    arr[int(sys.stdin.readline())] += 1
for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)
