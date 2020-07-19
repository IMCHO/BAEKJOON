N = int(input())
students = list(map(int, input().split()))
B, C = list(map(int, input().split()))
result = N
inital = [B] * N

for a, b in zip(students, inital):
    if a - b > 0:
        result += (((a - b) // C) + (1 if (a - b) % C != 0 else 0))

print(result)
