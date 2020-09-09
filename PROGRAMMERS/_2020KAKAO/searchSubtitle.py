from collections import defaultdict


def solution(words, queries):
    answer = []
    dictForQuery = dict()
    trie = Trie()
    trieForReverse = Trie()

    for word in words:
        trie.addWord(word)
        trieForReverse.addWord(word[::-1])

    for query in queries:
        if query not in dictForQuery.keys():
            if query.startswith("?"):
                dictForQuery[query] = trieForReverse.searchWord(query[::-1].split("?")[0], len(query))
            else:
                dictForQuery[query] = trie.searchWord(query.split("?")[0], len(query))

        answer.append(dictForQuery[query])
    return answer


class Node:
    def __init__(self):
        self.next = dict()
        self.length = defaultdict(int)


class Trie:
    def __init__(self):
        self.head = Node()
        self.cur = self.head

    def addWord(self, word):
        self.cur = self.head

        self.head.length[len(word)] += 1
        for c in word:
            if c not in self.cur.next.keys():
                newNode = Node()
                self.cur.next[c] = newNode
            self.cur = self.cur.next[c]
            self.cur.length[len(word)] += 1

    def searchWord(self, word, lenOfQ):
        self.cur = self.head

        for c in word:
            if c in self.cur.next.keys():
                self.cur = self.cur.next[c]
            else:
                return 0
        return self.cur.length[lenOfQ]
