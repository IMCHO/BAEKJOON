from copy import deepcopy


def solution(triangle):
    copiedTri = deepcopy(triangle)

    for index1, line in enumerate(copiedTri):
        if index1 == len(copiedTri) - 1: break
        for index2, value in enumerate(line):
            left = copiedTri[index1 + 1][index2]
            if index2 == 0:
                copiedTri[index1 + 1][index2] += value
            else:
                copiedTri[index1 + 1][index2] = max(left - line[index2 - 1] + value, left)
            copiedTri[index1 + 1][index2 + 1] += value

    return max(copiedTri.pop())


# solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
