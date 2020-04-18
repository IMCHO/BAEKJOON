'''
    Make a dictionary for map by '+5, -5, +1,-1'.
    Get a direction depending on '+5, -5, +1,-1'.
    Count how many changing direction until meeting hole.
    If it is under 10, get a minimum value.
    If these are all over 10, print -1.
    See where blue is moving to while red is moving.
'''


def BFS(graph, start, end):
    queue = [[[start, "X"], [start, ], 0]]
    result1 = []
    result2 = []
    while queue:
        informationOfSpot = queue.pop(0)
        if informationOfSpot[0][0] != end:
            for index in graph[informationOfSpot[0][0]]:
                if index[0] not in informationOfSpot[1]:
                    changeDirection = informationOfSpot[2]
                    if informationOfSpot[0][1] != index[1]: changeDirection += 1
                    temp = informationOfSpot[1][:]
                    temp.append(index[0])
                    queue.append([[index[0], index[1]], temp, changeDirection])
                if index[0] == end:
                    result1.append(temp)
                    result2.append(changeDirection)
    print(result1)
    print(result2)

    # Add direction


row, col = map(int, input().split())
graph = {}
map = ""
for _ in range(row):
    map += input()
# print(map)
for index, spot in enumerate(map):
    if spot == "#":
        continue
    if spot == "." or spot == "R" or spot == "B" or spot == "O":
        graph[index] = []
        if map[index + col] != "#":
            graph[index].append([index + col, "N"])
        if map[index - col] != "#":
            graph[index].append([index - col, "S"])
        if map[index + 1] != "#":
            graph[index].append([index + 1, "E"])
        if map[index - 1] != "#":
            graph[index].append([index - 1, "W"])
# print(graph)
indexOfRed = map.index('R')
indexOfBlue = map.index('B')
indexOfDestination = map.index('O')
BFS(graph, indexOfRed, indexOfDestination)
