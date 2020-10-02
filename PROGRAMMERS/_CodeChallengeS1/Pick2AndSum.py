from itertools import combinations


def solution(numbers):
    answer = set()
    for result in combinations(numbers, 2):
        answer.add(sum(result))
    return sorted(answer)
