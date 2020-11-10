import sys, heapq


def getParent(index):
    if index == pInfos[index]: return index
    return getParent(pInfos[index])


def check():
    value = getParent(0)
    for num in pInfos:
        if value != getParent(num):
            return False
    return True


global pInfos
N, M = map(int, sys.stdin.readline().strip().split())
queue = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    queue.append([C, A, B])

pInfos = [i for i in range(N)]
heapq.heapify(queue)
cost = 0

while queue:
    now = heapq.heappop(queue)
    p1, p2 = getParent(now[1] - 1), getParent(now[2] - 1)
    if p1 != p2:
        pInfos[p1] = min(p1, p2)
        pInfos[p2] = min(p1, p2)
        # print(pInfos)
        cost += now[0]
        if check():
            print(cost - now[0])
            break
# print(pInfos)