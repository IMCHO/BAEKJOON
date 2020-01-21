N, M = map(int, input().split())
deck = sorted(list(map(int, input().split())))
result = []
for firstIndex in range(0, N - 2):
    for secondIndex in range(firstIndex + 1, N - 1):
        for thirdIndex in range(secondIndex + 1, N):
            val = deck[firstIndex] + deck[secondIndex] + deck[thirdIndex]
            if val > M:
                break
            else:
                result.append(val)
print(max(result))
