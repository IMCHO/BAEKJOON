for _ in range(int(input())):
    x, y = (int(i) for i in input().split())
    recordOfUse = [1]
    x += recordOfUse[0]
    while True:
        if x > y:
            x -= recordOfUse.pop()
        elif x == y:
            if recordOfUse[len(recordOfUse) - 1] == 1:
                print(len(recordOfUse))
                break
            else:
                x -= recordOfUse.pop()
        move = recordOfUse[len(recordOfUse) - 1] + 1
        x += move
        recordOfUse.append(move)
