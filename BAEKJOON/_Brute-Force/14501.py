def work(start, cost):
    global T, P, result

    if start + T[start] > N:
        result = max(cost, result)
        return
    cost += P[start]
    result = max(cost, result)
    for day in range(start + T[start], N):
        work(day, cost)


global T, P, result
N = int(input())
T = []
P = []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

result = 0

for day in range(N):
    work(day, 0)

print(result)
