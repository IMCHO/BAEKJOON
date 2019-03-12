for _ in range(int(input())):
    x, y = (int(i) for i in input().split())
    maxMove = 2
    if y - 1 < x + 1:
        print("1")
    elif y - 1 == x + 1:
        print("2")
    else:
        remainDistance = y - 1 - (x + 1)
        while True:
            if remainDistance <= maxMove:
                print(maxMove + 1)
                break
            else:
                remainDistance -= maxMove
                maxMove += 1
