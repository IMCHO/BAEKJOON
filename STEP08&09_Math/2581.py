def isThisDecimal(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0: return False
        return True


m, n = int(input()), int(input())
arr = []
for i in range(m, n + 1):
    if isThisDecimal(i):
        arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
