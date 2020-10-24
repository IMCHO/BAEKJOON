def solution(n):
    cntList = [1, 2]

    if n == 1 or n == 2:
        return cntList[n - 1]
    else:
        while True:
            num = len(cntList) + 1
            cntList.append((cntList[num - 2] + cntList[num - 3]) % 1000000007)
            if num == n:
                answer = cntList.pop()
                break
    return answer
