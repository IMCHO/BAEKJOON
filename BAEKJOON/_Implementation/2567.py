n = int(input())
board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    left, bottom = map(int, input().split())
    for x in range(bottom, bottom + 10):
        for y in range(left, left + 10):
            board[x][y] = 1

offsets = [[1, 0], [-1, 0], [0, 1], [0, -1]]
length = 0
for x in range(100):
    for y in range(100):
        if board[x][y] == 1:
            for offset in offsets:
                newPoint = [x + offset[0], y + offset[1]]
                if newPoint[0] < 0 or newPoint[0] >= 100 or newPoint[1] < 0 or newPoint[1] >= 100:
                    length += 1
                    continue
                if board[newPoint[0]][newPoint[1]] == 0: length += 1

print(length)
