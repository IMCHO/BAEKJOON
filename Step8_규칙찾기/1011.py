for _ in range(int(input())):
    x, y = (int(i) for i in input().split())
    move=1
    x+=move
    timesOfUse=1
    while True:
        if x==y and move==1:
            print(timesOfUse)
            break
        