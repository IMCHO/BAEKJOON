for _ in range(int(input())):
    x, y = (int(i) for i in input().split())
    y, x = y - x, 0
    if y == 1:
        print(1)
    elif y == 2:
        print(2)
    else:
        print(((y-1)//2)+2)