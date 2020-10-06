def solution(lines):
    infos = []
    for line in lines:
        _, end, duration = line.split(" ")
        h, m, s = end.split(":")
        duration = duration.replace("s", "")
        if "." in duration:
            dS, dMS = duration.split(".")
        else:
            dS, dMS = duration, "0"
        S, MS = s.split(".")
        totalMSecOfEnd = int(h) * 3600000 + int(m) * 60000 + int(S) * 1000 + int(MS)
        totalMSecOfStart = totalMSecOfEnd - (int(dS) * 1000 + int(dMS)) + 1
        infos.append([totalMSecOfStart, totalMSecOfEnd])
    # print(infos)

    # maximum1 = 0
    # for info in infos:
    #     _, end = info
    #     temp1 = 1
    #     temp2 = 1
    #     endPlus1 = end + 999
    #     endMinus1 = end - 999
    #     for target in infos:
    #         if info == target: continue
    #         if target[0] <= endPlus1 <= target[1]:
    #             temp1 += 1
    #         if target[0] <= endMinus1 <= target[1]:
    #             temp2 += 1
    #
    #     maximum1 = max(temp1, temp2, maximum1)
    #
    # maximum2 = 0
    # infos = sorted(infos, key=lambda x: x[0])
    # for info in infos:
    #     start, end = info
    #     startPlus1 = start + 999
    #     startMinus1 = start - 999
    #     temp1 = 1
    #     temp2 = 1
    #     for target in infos:
    #         if info == target: continue
    #         if target[0] <= startPlus1 <= target[1]:
    #             temp1 += 1
    #         if target[0] <= startMinus1 <= target[1]:
    #             temp2 += 1
    #     maximum2 = max(temp1, temp2, maximum2)

    maximum = 0
    startTime = sorted(infos, key=lambda x: x[0])[0][0]
    for start in range(startTime if startTime >= 0 else 0, infos[len(infos) - 1][1] + 1):
        end = start + 999
        temp = 0
        for info in infos:
            if start <= info[0] <= end or start <= info[1] <= end:
                temp += 1
        maximum = max(maximum, temp)

    return maximum


print(solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]))
