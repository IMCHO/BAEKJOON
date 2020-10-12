from itertools import combinations
from copy import deepcopy
from collections import deque
import heapq


def solution(a):
    # copiedA = list(map(lambda x: [x[1], x[0]], enumerate(a)))
    # print(copiedA)
    # work(copiedA)
    result = []
    for index, element in enumerate(a):
        if index == 0 or index == len(a) - 1:
            result.append(element)
            continue
        front = a[:index]
        back = a[index + 1:]
        heapq.heapify(front)
        heapq.heapify(back)

        if heapq.heappop(front) < element and heapq.heappop(back) < element:
            continue
        else:
            result.append(element)

    return len(result)


# def work(l):
#     d = deque([[l, False]])
#     result = set()
#     # print(d.popleft())
#     while d:
#         target, isSmallerDead = d.popleft()
#         if len(target) == 1: result.add(target[0][0])
#         for element in combinations(target, 2):
#             first, second = element
#             if first[1] - second[1] != 1 and first[1] - second[1] != -1: continue
#             if isSmallerDead:
#                 newList = deepcopy(target)
#                 newList.remove(second if first[0] < second[0] else first)
#                 newList = list(map(lambda x: [x[1][0], x[0]], enumerate(newList)))
#                 if [newList, True] not in d:
#                     d.append([newList, True])
#             else:
#                 newList = deepcopy(target)
#                 newList.remove(second if first[0] < second[0] else first)
#                 newList = list(map(lambda x: [x[1][0], x[0]], enumerate(newList)))
#                 if [newList, False] not in d:
#                     d.append([newList, False])
#                 newList = deepcopy(target)
#                 newList.remove(second if first[0] > second[0] else first)
#                 newList = list(map(lambda x: [x[1][0], x[0]], enumerate(newList)))
#                 if [newList, True] not in d:
#                     d.append([newList, True])
#
#     return result


print(solution([9, -1, -5]))
