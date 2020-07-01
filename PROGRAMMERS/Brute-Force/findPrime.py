import itertools
import math


def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False

    for i in range(2, int(k) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    result = set()
    for cnt in range(1, len(numbers) + 1):
        temp = itertools.permutations(numbers, cnt)
        for t in temp:
            numStr = ''.join(t)
            if numStr[0] != '0': result.add(numStr)

    for num in result:
        if check(int(num)): answer += 1

    return answer
