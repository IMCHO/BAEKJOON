from collections import defaultdict
import heapq


def solution(N, road, K):
    infos = defaultdict(set)
    costList = [0] + [10001 for _ in range(N - 1)]

    for start, end, cost in road:
        infos[start].add((end, cost))
        infos[end].add((start, cost))

    heap = [[0, 1]]

    while heap:
        nextOne = heapq.heappop(heap)
        if nextOne[0] > K: continue
        for info in infos[nextOne[1]]:
            if costList[info[0] - 1] > nextOne[0] + info[1]:
                costList[info[0] - 1] = nextOne[0] + info[1]
                heapq.heappush(heap, [costList[info[0] - 1], info[0]])

    return len(list(filter(lambda x: x <= K, costList)))
