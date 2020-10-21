def solution(progresses, speeds):
    answer = []
    info = zip(progresses, speeds)

    while info:
        cnt = 0
        newInfo = []
        for progress, speed in info:
            progress += speed
            if progress >= 100:
                progress = 100
                if len(newInfo) == 0:
                    cnt += 1
                else:
                    newInfo.append([progress, speed])
            else:
                newInfo.append([progress, speed])
        if cnt != 0:
            answer.append(cnt)
        info = newInfo

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
