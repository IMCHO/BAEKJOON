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

def minHeapify(array):
    length=len(array)
    if length==1: return array
    elif length==2:




arr = []
for _ in range(int(input())): arr.append(int(input()))

# for i in mergeSort(arr):
#     print(i)
