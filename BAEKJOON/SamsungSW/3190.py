from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
directions = [input().split() for _ in range(L)]
offsetOfDir = [[0, -1], [-1, 0], [0, 1], [1, 0]]

map = [[0] * N for _ in range(N)]
for apple in apples:
    map[apple[0] - 1][apple[1] - 1] = 1

# for i in range(N):
#     for j in range(N):
#         print(map[i][j], end=' ')
#     print('\n')

snake = deque([[0, 0]])
time = 0
whichDir = 2

while 1:
    time += 1
    head = snake[0]
    for direction in directions:
        if time - 1 == int(direction[0]):
            if direction[1] == 'D':
                whichDir += 1
                if whichDir == 4: whichDir = 0
            else:
                whichDir -= 1
                if whichDir < 0: whichDir = 3
            directions.pop(0)
            break

    newHead = [head[0] + offsetOfDir[whichDir][0], head[1] + offsetOfDir[whichDir][1]]
    print(newHead[0], newHead[1])
    print('\n')
    for d in snake:
        print(d[0], d[1])
    print('\n')

    if newHead[0] >= N or newHead[0] < 0 or newHead[1] >= N or newHead[1] < 0:
        print("Collapse cuz of board", newHead[0], newHead[1])
        break

    if newHead in snake:
        print("Collapse cuz of snake")
        break

    snake.appendleft(newHead)

    if map[newHead[0]][newHead[1]] != 1:
        snake.pop()

print(time)
