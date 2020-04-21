import math


def isThisPrime(num):
    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0: return False
    return True


for _ in range(int(input())):
    n = int(input())
    a, b = n // 2, n // 2
    while True:
        if isThisPrime(a) and isThisPrime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1