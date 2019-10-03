def hanoi(n):
    if n == 1:
        cnt = 1
        progress = ["1 3"]
    else:
        lastCnt, lastPro = hanoi(n - 1)
        cnt = lastCnt * 2 + 1
        front = change(lastPro, "3", "2")
        back = change(lastPro, "2", "1")
        progress = front + ["1 3"] + back

    return cnt, progress


def change(arr, n1, n2):
    temp = []
    for i in arr:
        i = i.replace(n1, "0")
        i = i.replace(n2, n1)
        i = i.replace("0", n2)
        temp.append(i)
    return temp
    # return arr


n = int(input())
a, b = hanoi(n)
print(a)
print(i for i in b)
for i in b:
    print(i)
