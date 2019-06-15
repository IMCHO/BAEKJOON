# for i in sorted([int(input()) for _ in range(int(input()))]): print(i)

arr = []
for _ in range(int(input())): arr.append(int(input()))
for i in range(1, len(arr)):
    temp = arr[i]
    for j in range(i - 1, -1, -1):
        if temp < arr[j]:
            arr[j + 1], arr[j] = arr[j], temp
        else:
            break
for i in arr: print(i)
