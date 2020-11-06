import heapq

N, people = int(input()), list(map(int, input().split()))
heapq.heapify(people)
result = [0]

while people:
    p = heapq.heappop(people)
    result.append(result[-1] + p)

print(sum(result))
