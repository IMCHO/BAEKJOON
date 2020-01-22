def makeNewNum(n):
    listN = list(str(n))
    return n + sum(int(listN[i]) for i in range(len(listN)))


N = int(input())
r = 0
for num in range(1, N + 1):
    if N == makeNewNum(num):
        r = num
        break
print(r)