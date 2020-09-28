from collections import deque
from copy import deepcopy


def solution(routes):
    copiedRoutes = deque(sorted(routes, key=lambda x: (-x[0], -x[1])))
    # print(copiedRoutes)
    cnt = 0
    while copiedRoutes:
        start, end = copiedRoutes.popleft()
        cnt += 1
        cRouteForRemove = deepcopy(copiedRoutes)

        for start2, end2 in copiedRoutes:
            if start <= end2:
                cRouteForRemove.remove([start2, end2])
        copiedRoutes = cRouteForRemove

    return cnt
