from collections import deque, defaultdict

N, M = map(int, input().split())
numInfos = defaultdict(list)
lineInfos = {i: 0 for i in range(N)}
d = deque([])
result = []

for _ in range(M):
    start, end = map(int, input().split())
    numInfos[start - 1].append(end - 1)
    lineInfos[end - 1] += 1

for key, value in lineInfos.items():
    if value == 0:
        d.append(key)

while d:
    target = d.popleft()
    for value in numInfos[target]:
        lineInfos[value] -= 1
        if lineInfos[value] == 0:
            d.append(value)
    result.append(target)

print(" ".join(map(str, map(lambda x: x + 1, result))))
