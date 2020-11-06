n = int(input())
cntList = [1, 1, 2]
targetList = []
maxTarget = 0
for _ in range(n):
    target = int(input())
    maxTarget = max(target, maxTarget)
    targetList.append(target)

for i in range(3, maxTarget + 1):
    cntList.append(cntList[i - 3] + cntList[i - 2] + cntList[i - 1])

for i in targetList:
    print(cntList[i])
