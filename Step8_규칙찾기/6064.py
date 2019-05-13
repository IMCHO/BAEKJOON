for _ in range(int(input())):
    M, N, x, y = list(map(int, input().split()))
    bigNum, smlNum = max(M, N), min(M, N)
    diff = bigNum - smlNum
    arrOfMatch = [diff]
    num = diff
    while True:
        if num == smlNum:
            break
        num += diff
        if num > smlNum:
            num = num - smlNum
        arrOfMatch.append(num)
    if bigNum == M:
        try:
            if y + M - x > N:
                temp = arrOfMatch.index(y + M - x - N)
            else:
                temp = arrOfMatch.index(y + M - x)
        except:
            print(-1)
        else:
            print((temp + 1) * M - (M - x))
    else:
        try:
            if x + N - y > M:
                temp = arrOfMatch.index(x + N - y - M)
            else:
                temp = arrOfMatch.index(x + N - y)
        except:
            print(-1)
        else:
            print((temp + 1) * N - (N - y))
