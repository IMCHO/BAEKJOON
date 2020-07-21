from collections import defaultdict, deque
from copy import deepcopy


def solution(begin, target, words):
    if target not in words: return 0

    wordMap = defaultdict(list)

    for word in words:
        makeMap(wordMap, begin, word)

    for word in words:
        for target in words:
            if word == target: continue
            makeMap(wordMap, word, target)

    deq = deque([[begin, []]])

    while deq:
        info = deq.popleft()

        for next in wordMap[info[0]]:
            if next in info[1]: continue
            if next == target: return len(info[1]) + 1

            newRoute = deepcopy(info[1])
            newRoute.append(info[0])
            newInfo = [next, newRoute]
            deq.append(newInfo)

            print("now : " + next)
            print("before : " + ' '.join(newRoute))

    return 0


def makeMap(wordMap, index, word):
    cnt = 0
    for c in index:
        if c in word: cnt += 1
    if cnt == 2: wordMap[index].append(word)
