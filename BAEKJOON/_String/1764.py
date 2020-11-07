from collections import defaultdict

N, M = map(int, input().split())
names = defaultdict(int)
result = []

for _ in range(N):
    names[input()] = 1

for _ in range(M):
    name = input()
    if names[name] == 1:
        result.append(name)

print(len(result))
for name in sorted(result):
    print(name)
