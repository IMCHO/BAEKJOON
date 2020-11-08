from collections import defaultdict
import heapq, sys

V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())
infos = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    infos[u].append([w, v])

MAXINT = sys.maxsize
costList = [MAXINT] * V
costList[K - 1] = 0

queue = [[0, K]]
heapq.heapify(queue)

while queue:
    now = heapq.heappop(queue)
    if now[0] > costList[now[1] - 1]: continue
    for nextOne in infos[now[1]]:
        cost, nextV = nextOne
        newValue = now[0] + cost
        if costList[nextV - 1] >= newValue:
            costList[nextV - 1] = newValue
            heapq.heappush(queue, [newValue, nextV])

for i in costList:
    if i == MAXINT:
        print("INF")
    else:
        print(i)
