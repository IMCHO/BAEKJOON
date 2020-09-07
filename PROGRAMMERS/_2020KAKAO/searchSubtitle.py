import re


def solution(words, queries):
    answer = []

    for query in queries:
        cntOfQMark = query.count("?")
        if query.startswith("?"):
            pattern = "[a-z]" + "{" + str(cntOfQMark) + "}" + query[query.rfind("?") + 1:]
        else:
            pattern = query[0:query.find("?")] + "[a-z]" + "{" + str(cntOfQMark) + "}"
        regex = re.compile(pattern)
        result = regex.findall(" ".join(filter(lambda x: len(x) == len(query), words)))
        answer.append(len(set(result)))
    return answer
