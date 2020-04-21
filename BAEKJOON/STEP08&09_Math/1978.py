n = int(input())
arr = list(map(int, input().split()))
cnt = 0
flag = 0
for i in arr:
    if i == 1: continue
    if i == 2:
        cnt += 1
        continue
    for j in range(2, i):
        if i % j == 0:
            flag = 1
            break
    if flag == 1:
        flag = 0
    else:
        cnt += 1
print(cnt)
