# for i in sorted([int(input()) for _ in range(int(input()))]): print(i)

# arr = []
# for _ in range(int(input())): arr.append(int(input()))
# for i in range(1, len(arr)):
#     temp = arr[i]
#     for j in range(i - 1, -1, -1):
#         if temp < arr[j]:
#             arr[j + 1], arr[j] = arr[j], temp
#         else:
#             break
# for i in arr: print(i)

# arr = []
# for _ in range(int(input())): arr.append(int(input()))
# i = 0
# count = 0
# while True:
#     try:
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]
#         else:
#             count += 1
#     except:
#         if len(arr) == 1:
#             break
#         else:
#             i, count = 0, 0
#             continue
#     i += 1
#     if count == len(arr) - 1: break
# for i in arr: print(i)
# -------------------------------------------------------------------------- Insert Sort

arr = []
for _ in range(int(input())): arr.append(int(input()))

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in arr: print(i)