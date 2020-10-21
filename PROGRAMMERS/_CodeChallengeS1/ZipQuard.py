def solution(arr):
    global cntOf0, cntOf1
    cntOf0 = 0
    cntOf1 = 0
    length = len(arr)

    work(arr, 0, length - 1, 0, length - 1)

    return [cntOf0, cntOf1]


def work(arr, startOfX, endOfX, startOfY, endOfY):
    global cntOf1, cntOf0
    target = arr[startOfX][startOfY]

    for x in range(startOfX, endOfX + 1):
        for y in range(startOfY, endOfY + 1):
            if target != arr[x][y]:
                diffX = (endOfX - startOfX) // 2
                diffY = (endOfY - startOfY) // 2
                work(arr, startOfX, startOfX + diffX, startOfY, startOfY + diffY)
                work(arr, startOfX, startOfX + diffX, endOfY - diffY, endOfY)
                work(arr, endOfX - diffX, endOfX, startOfY, startOfY + diffY)
                work(arr, endOfX - diffX, endOfX, endOfY - diffY, endOfY)
                return

    if target == 1:
        cntOf1 += 1
    else:
        cntOf0 += 1


# print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
