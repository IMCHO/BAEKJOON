for _ in range(int(input())):
    H, W, N = list(map(int, input().split()))
    room = [1, 0, 1]
    for _ in range(1, N):
        if room[0] >= H:
            room[0] = 1
            room[2] += 1
            if room[2] > 9:
                room[1] += 1
                room[2] = 0
        else:
            room[0] += 1
    print("".join(list(map(str, room))))