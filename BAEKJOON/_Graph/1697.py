import sys
from collections import deque, defaultdict

N, K = map(int, sys.stdin.readline().strip().split())
queue = deque([[N, 0]])
result = 0
visited = defaultdict(int)
while queue:
    now = queue.popleft()
    visited[now[0]] = 1
    if now[0] == K:
        result = now[1]
        break

    for newPos in [now[0] + 1, now[0] - 1, now[0] * 2]:
        if 0 <= newPos <= 100000 and visited[newPos] == 0:
            queue.append([newPos, now[1] + 1])

print(result)
