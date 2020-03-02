def mergeSort(array):
    # print(array)
    length = len(array)
    if length <= 2:
        return array
    else:
        mid = length // 2
        temp = []
        left = mergeSort(array[0:mid])
        right = mergeSort(array[mid:length])
        tempLen = len(left) if len(left) < len(right) else len(right)

        return temp
        # return mergeSort(array[0:mid]) + mergeSort(array[mid:length])


# def mergeSort2(left,right):


arr = []
for _ in range(int(input())): arr.append(int(input()))
print(mergeSort(arr))
