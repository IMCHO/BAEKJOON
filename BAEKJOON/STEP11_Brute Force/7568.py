# guys = []
# for _ in range(int(input())):
#     guys.append(list(map(int, input().split())))
guys = [list(map(int, input().split())) for _ in range(int(input()))]
for i in range(len(guys)):
    rank = 1
    for j in range(len(guys)):
        if i == j: continue
        if guys[i][0] < guys[j][0] and guys[i][1] < guys[j][1]: rank += 1
    print(rank, end=' ')
#     guys[i].append(rank)
# for i in range(len(guys)):
#     print(guys[i][2], end=' ')
