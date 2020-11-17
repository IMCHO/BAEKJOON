from sys import stdin
from collections import defaultdict, deque

N, M, V = map(int, stdin.readline().strip().split())
infos = defaultdict(set)

for _ in range(M):
    a, b = map(int, stdin.readline().strip().split())
    infos[a].add(b)
    infos[b].add(a)


def DFS(start, isVisited, result):
    result.append(start)
    isVisited[start] = 1

    for nextOne in sorted(list(infos[start])):
        if isVisited[nextOne] == 0:
            isVisited[nextOne] = 1
            DFS(nextOne, isVisited, result)


result = []
isVisited = defaultdict(int)
DFS(V, isVisited, result)

print(" ".join(map(str, result)))

queue = deque([V])
isVisited = defaultdict(int)
result = []

while queue:
    now = queue.popleft()
    result.append(now)
    isVisited[now] = 1

    for nextOne in sorted(list(infos[now])):
        if isVisited[nextOne] == 0:
            isVisited[nextOne] = 1
            queue.append(nextOne)

print(" ".join(map(str, result)))
