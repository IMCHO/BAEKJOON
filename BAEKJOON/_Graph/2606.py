def getParent(index):
    if index == pInfos[index - 1]: return index
    return getParent(pInfos[index - 1])


N, cntOfLines = int(input()), int(input())
pInfos = [i for i in range(1, N + 1)]
for _ in range(cntOfLines):
    n1, n2 = map(int, input().split())
    maxNum, minNum = max(getParent(n1), getParent(n2)), min(getParent(n1), getParent(n2))
    pInfos[maxNum - 1] = minNum
# print(pInfos)

cnt = 0
for i in pInfos:
    if getParent(i) == 1: cnt += 1

print(cnt - 1)
