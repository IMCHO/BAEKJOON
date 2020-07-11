def solution(scoville, K):
    answer = 0

    for i in range(len(scoville) // 2 - 1, -1, -1):
        heapify(scoville, i, len(scoville))

    while len(scoville) != 1:
        if len(list(filter(lambda x: x < K, scoville))) == 0: break

        scoville[0], scoville[len(scoville) - 1] = scoville[len(scoville) - 1], scoville[0]
        s1 = scoville.pop()
        heapify(scoville, 0, len(scoville))

        scoville[0], scoville[len(scoville) - 1] = scoville[len(scoville) - 1], scoville[0]
        s2 = scoville.pop()
        heapify(scoville, 0, len(scoville))

        scoville.append(s1 + s2 * 2)
        answer += 1

    if scoville[0] < K: return -1
    return answer


def heapify(tree, start, size):
    smallest = start
    left = start * 2 + 1
    right = start * 2 + 2
    if left < size and tree[smallest] > tree[left]: smallest = left
    if right < size and tree[smallest] > tree[right]: smallest = right
    if smallest != start:
        tree[smallest], tree[start] = tree[start], tree[smallest]
        heapify(tree, smallest, size)
