import sys
from itertools import permutations


def DFS(nums, index1, operation, index2, result):
    global maxNum, minNum
    if index1 == len(nums):
        maxNum = max(maxNum, result)
        minNum = min(minNum, result)
        return

    if operation[index2] == "+":
        result += nums[index1]
    elif operation[index2] == "-":
        result -= nums[index1]
    elif operation[index2] == "/":
        if result < 0:
            result = -((-1 * result) // nums[index1])
        else:
            result = result // nums[index1]
    else:
        result *= nums[index1]

    # if maxNum < result:
    #     DFS(nums, index1 + 1, operation, index2 + 1, result)
    # elif result < minNum:
    DFS(nums, index1 + 1, operation, index2 + 1, result)
    # else:
    #     return


global maxNum, minNum
N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
operationInfos = list(map(int, sys.stdin.readline().strip().split()))
operations = []
for _ in range(operationInfos[0]):
    operations.append("+")
for _ in range(operationInfos[1]):
    operations.append("-")
for _ in range(operationInfos[2]):
    operations.append("*")
for _ in range(operationInfos[3]):
    operations.append("/")

maxNum = -1000000001
minNum = 1000000001
for operation in set(permutations(operations, len(operations))):
    DFS(nums, 1, operation, 0, nums[0])

print(maxNum)
print(minNum)
