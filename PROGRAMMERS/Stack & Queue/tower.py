from collections import deque


def solution(heights):
    answer = deque()
    while len(heights):
        temp = heights.pop()
        answer.appendleft(0)
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > temp:
                answer.popleft()
                answer.appendleft(i + 1)
                break

    return list(answer)
