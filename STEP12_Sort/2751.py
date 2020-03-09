def mergeSort(array):
    # print(array)
    length = len(array)
    if length == 1:
        return array
    else:
        mid = length // 2
        temp = []
        left = mergeSort(array[0:mid])
        right = mergeSort(array[mid:length])

        # print("left: {0}".format(left))
        # print("right: {0}".format(right))

        for leftValue in left:
            if leftValue == 0: continue
            for rightValue in right:
                if rightValue == 0: continue
                if leftValue < rightValue:
                    temp.append(leftValue)
                    left[left.index(leftValue)] = 0
                    break
                else:
                    temp.append(rightValue)
                    right[right.index(rightValue)] = 0

        left = dealWithZero(left)
        right = dealWithZero(right)

        # print("after left: {0}".format(left))
        # print("after right: {0}".format(right))

        if len(left) != 0:
            temp += left
        elif len(right) != 0:
            temp += right

        # print("temp: {0}".format(temp))

        return temp
        # return mergeSort(array[0:mid]) + mergeSort(array[mid:length])


def dealWithZero(arr):
    if arr.count(0) >= 1:
        arr = set(arr)
        arr.remove(0)
        return list(arr)
    return arr


arr = []
for _ in range(int(input())): arr.append(int(input()))
for i in mergeSort(arr):
    print(i)
