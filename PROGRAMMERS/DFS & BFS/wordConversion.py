from collections import defaultdict


def solution(begin, target, words):
    answer = 0
    if target not in words: return 0

    wordMap = defaultdict(list)

    for word in words:
        cnt = 0
        for c in begin:
            if c in word: cnt += 1
        if cnt == 2: wordMap[begin].append(word)

    for word in words:
        for target in words:
            if word == target: continue
            cnt = 0
            for c in target:
                if c in word: cnt += 1
            if cnt == 2: wordMap[word].append(target)

    # for word in wordMap:
    #     print(word, end=' : ')
    #     for i in wordMap[word]:
    #         print(i, end=' ')
    #     print('\n')

    return answer
