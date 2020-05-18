def solution(numbers):
    answer = 0

    tempStr=''.join(sorted(list(numbers),reverse=True))
    maxNum=int(tempStr)

    for n in range(maxNum):
        if ''.join(sorted(list(n),reverse=True)) in tempStr:

    return answer