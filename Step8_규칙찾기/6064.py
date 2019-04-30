for _ in range(int(input())):
    M, N, x, y = list(map(int, input().split()))
    i = 1
    maxY, minY = max(M, N), min(M, N)
    while True:
        init = maxY * i - minY * i
        if init < 0:
            print(-1)
            break
        if maxY == M:
            temp = M - x
            init -= temp
            if init <= 0:
                init = N - init
                if init == y:
                    break
                else:
                    i += 1
                    continue
            else:
                if init == y:
                    break
                else:
                    i += 1
                    continue
        else:
            temp = N - y
            init -= temp
            if init <= 0:
                init = M - init
                if init == x:
                    break
                else:
                    i += 1
                    continue
            else:
                if init == x:
                    break
                else:
                    i += 1
                    continue
    print(i * maxY - temp)
