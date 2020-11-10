import sys


def DFS(nums, index, pickCnt, result):
    if pickCnt == 0:
        print(" ".join(map(str, result)))
        return

    for i in range(index, len(nums) - pickCnt + 1):
        result.append(nums[i])
        DFS(nums, i + 1, pickCnt - 1, result)
        result.pop()


pickCnt = 6
while True:
    inputData = list(map(int, sys.stdin.readline().strip().split()))
    k = inputData[0]
    if k == 0: break
    nums = inputData[1:]
    DFS(nums, 0, pickCnt, [])
    print("")
