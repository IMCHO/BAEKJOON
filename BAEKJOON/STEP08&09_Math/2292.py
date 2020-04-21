num = int(input())
if num == 1:
    print(1)
else:
    for i in range(0, 50000):
        if pow(i, 2) * 3 + 3 * i + 2 <= num and pow(i + 1, 2) * 3 + 3 * (i + 1) + 2 > num:
            print(i + 2)
            break
