def solution(citations):
    answer = 0
    maxNum = len(citations)
    while maxNum:
        list_biggerThanMax = [i for i in citations if i >= maxNum]
        list_smallerThanMax = [i for i in citations if i <= maxNum and i not in list_biggerThanMax]
        if len(list_biggerThanMax) >= maxNum and len(list_smallerThanMax) <= maxNum:
            return maxNum
        maxNum -= 1
    return answer
