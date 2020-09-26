from collections import defaultdict
import heapq
import sys


def solution(n, edge):
    infos = defaultdict(set)
    costList = [0] + [sys.maxsize for _ in range(n - 1)]
    visited = [False for _ in range(n)]
    heap = [[0, 0]]
    for node, next in edge:
        infos[node - 1].add(next - 1)
        infos[next - 1].add(node - 1)

    while heap:
        smallest = heapq.heappop(heap)
        cost = smallest[0]
        node = smallest[1]

        if visited[node]:
            continue
        else:
            visited[node] = True

        for element in infos[node]:
            minimum = min(cost + 1, costList[element])
            costList[element] = minimum
            heapq.heappush(heap, [minimum, element])

    return costList.count(max(costList))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))