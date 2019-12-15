while True:
    lines = sorted(list(map(int, input().split())))
    if lines[0] == 0: break
    if lines[2] ** 2 == lines[1] ** 2 + lines[0] ** 2:
        print('right')
    else:
        print('wrong')
