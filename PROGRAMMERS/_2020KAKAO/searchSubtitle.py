import re


def solution(words, queries):
    # answer = []
    # d = {}
    # for query in queries:
    #     if query not in d.keys():
    #         cntOfQMark = query.count("?")
    #         if query.startswith("?"):
    #             pattern = "[a-z]" + "{" + str(cntOfQMark) + "}" + query[query.rfind("?") + 1:]
    #         else:
    #             pattern = query[0:query.find("?")] + "[a-z]" + "{" + str(cntOfQMark) + "}"
    #         regex = re.compile(pattern)
    #         result = regex.findall(" ".join(filter(lambda x: len(x) == len(query), words)))
    #         d[query] = len(set(result))
    #
    #     answer.append(d[query])
    # return answer
    trie = Trie()
    for word in words:
        trie.addWord(word)
    print(trie)


class Node:
    def __init__(self):
        self.value = ""
        self.next = dict()


class Trie:
    def __init__(self):
        self.head = Node()
        self.cur = self.head

    def addWord(self, word):
        for c in word:
            if c not in self.cur.next.keys():
                newNode = Node()
                newNode.value = c
                self.cur.next[c] = newNode
            self.cur = self.cur.next[c]

        self.cur = self.head

    def searchWord(self, word):
        for c in word:
            if c == "?":
