import math


def isThisPrimeByEratos(n):
    if n == 1:
        return False
    else:
        for i in range(2, math.trunc(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True


a, b = map(int, input().split())
for i in range(a, b + 1):
    if isThisPrimeByEratos(i): print(i)
