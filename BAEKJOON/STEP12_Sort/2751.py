def mergeSort(array):
    length = len(array)
    if length == 1:
        return array
    else:
        mid = length // 2
        temp = []
        left = mergeSort(array[0:mid])
        right = mergeSort(array[mid:length])

        LIndex, RIndex = 0, 0
        while len(left) > 0 and len(right) > 0:
            if left[LIndex] > right[RIndex]:
                temp.append(right.pop(RIndex))
            else:
                temp.append(left.pop(LIndex))

        if len(left) != 0:
            temp += left
        elif len(right) != 0:
            temp += right

        return temp


def heapSort(array):
    length = len(array)
    for index in range(length // 2 - 1, -1, -1):
        maxHeapify(array, index, length)

    for index in range(length - 1, 0, -1):
        array[0], array[index] = array[index], array[0]
        maxHeapify(array, 0, index)

    return array


def maxHeapify(array, parentIndex, heapSize):
    doesChangeHappen = False
    indexOfLargest = parentIndex
    leftChildIndex = parentIndex * 2 + 1
    rightChildIndex = parentIndex * 2 + 2

    if leftChildIndex < heapSize and array[leftChildIndex] > array[indexOfLargest]:
        indexOfLargest = leftChildIndex
        doesChangeHappen = True
    if rightChildIndex < heapSize and array[rightChildIndex] > array[indexOfLargest]:
        indexOfLargest = rightChildIndex
        doesChangeHappen = True

    if doesChangeHappen:
        array[indexOfLargest], array[parentIndex] = array[parentIndex], array[indexOfLargest]
        maxHeapify(array, indexOfLargest, heapSize)


arr = []
for _ in range(int(input())): arr.append(int(input()))

# for i in mergeSort(arr):
#     print(i)

for i in heapSort(arr):
    print(i)
