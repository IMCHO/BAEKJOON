import math
import sys


def isThisPrimeByEratos2(n):
    arr = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i + i, n + 1, i):
            arr[j] = False
    return len([i for i in range(1, n + 1) if arr[i]])


n = int(sys.stdin.readline())
while n:
    print(isThisPrimeByEratos2(2 * n) - isThisPrimeByEratos2(n))
    n = int(sys.stdin.readline())
