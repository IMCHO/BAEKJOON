n = int(input())
cntList = [0, 1, 1]
if len(cntList) >= n:
    print(cntList[n - 1])
else:
    while True:
        num = len(cntList) + 1
        minList = [cntList[num - 1 - 1] + 1]
        if num % 3 == 0:
            minList.append(cntList[num // 3 - 1] + 1)
        if num % 2 == 0:
            minList.append(cntList[num // 2 - 1] + 1)

        cntList.append(min(minList))
        if num == n:
            print(cntList.pop())
            break
