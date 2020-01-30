def checkBoard(sample, board, col):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if sample[i][col:col + 8][j] != board[i][j]: count += 1
    return count


board1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
board2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

M, N = map(int, input().split())
sample = []
for _ in range(M):
    sample.append(' '.join(input()).split(' '))

counts = []
for startRow in range(M - 7):
    for startCol in range(N - 7):
        count1 = 0
        count2 = 0
        count1 += checkBoard(sample[startRow:startRow + 8], board1, startCol)
        count2 += checkBoard(sample[startRow:startRow + 8], board2, startCol)
        counts.append(count1)
        counts.append(count2)
print(min(counts))
