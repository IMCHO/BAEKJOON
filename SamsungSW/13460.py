'''
    Make a dictionary for map by '+5, -5, +1,-1'.
    Get a direction depending on '+5, -5, +1,-1'.
    Count how many changing direction until meeting hole.
    If it is under 10, get a minimum value.
    If these are all over 10, print -1.
    See where blue is moving to while red is moving.
'''


def BFS(graph, start, end):
    queue = [[start, [start]]]
    result = []
    while queue:
        informationOfSpot = queue.pop(0)
        if informationOfSpot[0] != end:
            for index in graph[informationOfSpot[0]]:
                if index not in informationOfSpot[1]:
                    temp = informationOfSpot[1][:]
                    temp.append(index)
                    queue.append([index, temp])
                if index == end:
                    result.append(temp)
    print(result)

    # Add direction


row, col = map(int, input().split())
graph = {}
map = ""
for _ in range(row):
    map += input()
for index, spot in enumerate(map):
    if spot == "#":
        continue
    if spot == "." or spot == "R" or spot == "B" or spot == "O":
        graph[index] = []
        if map[index + 5] != "#":
            graph[index].append(index + 5)
        if map[index - 5] != "#":
            graph[index].append(index - 5)
        if map[index + 1] != "#":
            graph[index].append(index + 1)
        if map[index - 1] != "#":
            graph[index].append(index - 1)

indexOfRed = map.index('R')
indexOfBlue = map.index('B')
indexOfDestination = map.index('O')
BFS(graph, indexOfRed, indexOfDestination)
