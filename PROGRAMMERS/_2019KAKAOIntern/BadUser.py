import re
from copy import deepcopy


def solution(user_id, banned_id):
    global result
    answer = 1
    result = list()
    candidates = list()
    for b in banned_id:
        p = re.compile("^" + b.replace("*", ".", b.count("*")) + "$")
        s = set()
        for u in user_id:
            m = p.match(u)
            if m:
                s.add(m.group())
        candidates.append(s)
    # print(candidates)

    DFS(0, candidates, set())
    # print(result)

    return len(result)


def DFS(depth, candidates, s):
    global result
    if depth == len(candidates):
        print(s)
        if depth == len(s) and s not in result:
            result.append(deepcopy(s))
        return

    for candidate in candidates[depth]:
        if candidate not in s:
            s.add(candidate)
            DFS(depth + 1, candidates, s)
            s.remove(candidate)