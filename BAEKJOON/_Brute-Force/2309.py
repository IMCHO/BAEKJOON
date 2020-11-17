from sys import stdin


def DFS(resultValue, resultArr, cnt, isPicked, heights):
    global r
    if cnt == 2:
        if resultValue == 100:
            r = resultArr[:]
        return

    for targetIndex, height in enumerate(heights):
        if not isPicked[targetIndex]:
            isPicked[targetIndex] = True
            resultArr.append(height)
            DFS(resultValue - height, resultArr, cnt + 1, isPicked, heights)
            isPicked[targetIndex] = False
            resultArr.pop()


global r
r = []
heights = []

for _ in range(9):
    heights.append(int(stdin.readline().strip()))

isPicked = [False] * 9

DFS(sum(heights), [], 0, isPicked, heights)

heights = list(filter(lambda x: x not in r, heights))
for i in sorted(heights):
    print(i)
