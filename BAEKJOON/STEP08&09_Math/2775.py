room = [[0 for i in range(14)] for j in range(15)]
room[0] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for i in range(1, 15):
    for j in range(14):
        room[i][j] = sum(room[i - 1][0:j + 1])
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(room[k][n - 1])
