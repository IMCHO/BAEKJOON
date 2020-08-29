def solution(s):
    answer = []
    length = len(s)
    answer.append(length)

    for num in range(length - 1, 0, -1):
        copiedS = s
        result = ""
        cnt = 0

        while len(copiedS) != 0:
            temp = copiedS[0:num]
            copiedS = copiedS[num:]
            cnt += 1

            if len(copiedS) < num:
                result += (str(cnt) if cnt != 1 else "")
                result += temp
                result += copiedS
                break

            if copiedS.startswith(temp):
                continue
            else:
                result += (str(cnt) if cnt != 1 else "")
                result += temp
                cnt = 0

        answer.append(len(result))

    return min(answer)
