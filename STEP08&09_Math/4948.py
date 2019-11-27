import math
import sys


def isThisPrimeByEratos(n):
    if n == 1:
        return False
    else:
        for i in range(2, math.trunc(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True


n = int(sys.stdin.readline())
while n:
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if isThisPrimeByEratos(i): cnt += 1
    print(cnt)
    n = int(sys.stdin.readline())
