import sys, heapq
from collections import defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

infos = defaultdict(list)

for _ in range(M):
    n1, n2, cost = map(int, sys.stdin.readline().strip().split())
    infos[n1].append([n2, cost])

start, dest = map(int, sys.stdin.readline().strip().split())
costList = [sys.maxsize] * N
costList[start - 1] = 0

queue = [[0, start]]
heapq.heapify(queue)

while queue:
    c1, s = heapq.heappop(queue)
    if c1 > costList[s - 1]: continue

    for nextOne in infos[s]:
        d, c2 = nextOne
        newValue = c1 + c2
        if costList[d - 1] > newValue:
            costList[d - 1] = newValue
            heapq.heappush(queue, [newValue, d])

print(costList[dest - 1])
