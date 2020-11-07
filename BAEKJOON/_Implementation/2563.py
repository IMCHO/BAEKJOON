n = int(input())
board = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(n):
    left, bottom = map(int, input().split())
    for x in range(bottom, bottom + 10):
        for y in range(left, left + 10):
            board[x][y] = 1

cnt = 0
for x in range(100):
    for y in range(100):
        if board[x][y] == 1:
            cnt += 1
print(cnt)
