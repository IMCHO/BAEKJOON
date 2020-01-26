def checkBoard(sample, board):
    count = 0
    for i in range(len(board)):
        if sample[i] != board[i]: count += 1
    return count


board1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
board2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

M, N = map(int, input().split())
sample = []
for _ in range(M):
    sample.append(' '.join(input()).split(' '))

counts = []
for startRow in range(M - 7):
    for startCol in range(N - 7):
        count1 = 0
        count2 = 0
        for row in sample[startRow:startRow + 8]:
            count1 += checkBoard(row[startCol:startCol + 8], board1)
            count2 += checkBoard(row[startCol:startCol + 8], board2)
        counts.append(count1)
        counts.append(count2)
print(min(counts))
