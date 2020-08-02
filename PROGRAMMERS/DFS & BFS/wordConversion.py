from collections import defaultdict, deque
from copy import deepcopy


def solution(begin, target, words):
    if target not in words: return 0

    wordMap = defaultdict(set)

    for word in words:
        makeMap(wordMap, begin, word)

    for word in words:
        for nextWord in words:
            if word == nextWord: continue
            makeMap(wordMap, word, nextWord)

    deq = deque([[begin, [begin]]])

    # result = []

    while deq:
        info = deq.popleft()

        for nextWord in wordMap[info[0]]:
            # print(nextWord)
            # print(target)
            if nextWord in info[1]: continue
            if nextWord == target:
                return len(info[1])
                # result.append(len(info[1]))
                # continue

            newRoute = deepcopy(info[1])
            newRoute.append(nextWord)
            newInfo = [nextWord, newRoute]
            deq.append(newInfo)

            # print("now : " + nextWord)
            # print("before : " + ' '.join(newRoute))

    # return min(result) if len(result) != 0 else 0
    return 0


def makeMap(wordMap, index, word):
    cnt = 0
    for c1, c2 in zip(index, word):
        if c1 == c2: cnt += 1
    if cnt == len(word) - 1: wordMap[index].add(word)
