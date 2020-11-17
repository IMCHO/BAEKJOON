from sys import stdin
from collections import defaultdict


def DFS(cnt, N, d1, d2, d3):
    global result
    if cnt == N:
        result += 1
        return
    for index in range(N):
        if d1[cnt + index] == 0 and d2[cnt - index] == 0 and d3[index] == 0:
            d1[cnt + index] = 1
            d2[cnt - index] = 1
            d3[index] = 1
            DFS(cnt + 1, N, d1, d2, d3)
            d1[cnt + index] = 0
            d2[cnt - index] = 0
            d3[index] = 0


global result
result = 0
N = int(stdin.readline().strip())
DFS(0, N, defaultdict(int), defaultdict(int), defaultdict(int))
print(result)
