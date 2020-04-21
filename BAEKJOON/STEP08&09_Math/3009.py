resultOfX = []
resultOfY = []
for _ in range(3):
    x, y = map(int, input().split())
    resultOfX.remove(x) if resultOfX.count(x) >= 1 else resultOfX.append(x)
    resultOfY.remove(y) if resultOfY.count(y) >= 1 else resultOfY.append(y)
print(resultOfX[0], resultOfY[0])
