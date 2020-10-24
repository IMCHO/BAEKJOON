N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if graph[start][mid] and graph[mid][end]:
                graph[start][end] = 1

for i in range(N):
    for j in range(N):
        print(graph[i][j],end=" ")
    print("")
