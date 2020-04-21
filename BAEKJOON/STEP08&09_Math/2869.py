a, b, v = list(map(int, input().split()))
ans = (v - b) // (a - b)
temp = (v - b) % (a - b)
print(ans if temp == 0 else ans + 1)
