for _ in range(int(input())):
    x, y = (int(i) for i in input().split())
    y, x = y - x, 0
    start, count = 1, 0
    while start <= y:
        count += 1
        start += ((count // 2) if count % 2 == 0 else (count // 2) + 1)
    print(count)