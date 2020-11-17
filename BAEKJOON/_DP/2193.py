import sys

# def DFS(str, length):
#     global N, cnt
#     if length == N:
#         cnt += 1
#         return
#
#     if str[-1] == "0":
#         DFS(str + "0", length + 1)
#         DFS(str + "1", length + 1)
#     else:
#         DFS(str + "0", length + 1)


# global N, cnt
# cnt = 0
N = int(sys.stdin.readline().strip())
# DFS("1", 1)
#
# print(cnt)

cntList = [1, 1, 2]

for index in range(3, 90):
    cntList.append(cntList[index - 2] + cntList[index - 1])

print(cntList[N - 1])
