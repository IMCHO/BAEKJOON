import heapq


def solution(operations):
    answer = []
    rmMaxCmd = "D 1"
    rmMinCmd = "D -1"
    heapq.heapify(answer)

    for operation in operations:
        if operation == rmMaxCmd:
            if len(answer) == 0: continue
            answer = list(map(lambda x: (-x[0], x[0]), answer))
            heapq.heapify(answer)
            heapq.heappop(answer)

            answer = list(map(lambda x: (x[1], x[1]), answer))
            heapq.heapify(answer)
        elif operation == rmMinCmd:
            if len(answer) == 0: continue
            heapq.heappop(answer)
        else:
            value = int(operation.split(" ")[1])
            heapq.heappush(answer, (value, value))

    if len(answer) == 0:
        return [0, 0]
    else:
        answer = list(map(lambda x: (-x[0], x[0]), answer))
        heapq.heapify(answer)
        first = heapq.heappop(answer)
        heapq.heappush(answer, first)
        answer = list(map(lambda x: (x[1], x[1]), answer))
        heapq.heapify(answer)
        second = heapq.heappop(answer)
        return [-first[0], second[0]]


# print(solution(["I 7", "I 5", "I -5", "D -1"]))
# print(solution(["I 16", "D 1"]))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
