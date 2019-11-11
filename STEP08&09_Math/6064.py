for _ in range(int(input())):
    M, N, x, y = list(map(int, input().split()))
    bigNum, smlNum = max([M, x], [N, y]), min([M, x], [N, y])  # max/min 함수에 배열을 넣으면 첫번째 인자를 기준으로 판단한다! 같으면 다음 인자로 넘어감!
    diff = bigNum[0] - smlNum[0]
    diff = diff if diff != 0 else bigNum[0]
    while diff > smlNum[0]:
        diff -= smlNum[0]
    arrOfMatch = [diff]
    num = diff
    while True:
        if num == smlNum[0]:
            break
        num += diff
        if num > smlNum[0]:
            num = num - smlNum[0]
        arrOfMatch.append(num)
    temp = bigNum[0] - bigNum[1] + smlNum[1]
    while temp > smlNum[0]:
        temp -= smlNum[0]
    try:
        loc = arrOfMatch.index(temp)
    except:
        print(-1)
    else:
        print((loc + 1) * bigNum[0] - (bigNum[0] - bigNum[1]))
