from copy import deepcopy


def solution(key, lock):
    global M, N
    M = len(key)
    N = len(lock)
    length = M + N + M - 2
    expendedLock = [[0] * (M - 1) + list + [0] * (M - 1) for list in lock]

    for _ in range(M - 1):
        expendedLock.insert(0, [0] * length)
        expendedLock.append([0] * length)

    # print(expendedLock)

    return puzzle(key, expendedLock) or puzzle(rotate(key), expendedLock) or puzzle(rotate(rotate(key)),
                                                                                    expendedLock) or puzzle(
        rotate(rotate(rotate(key))), expendedLock)


# 오른쪽으로 90도 회전
def rotate(key):
    length = len(key)
    newKey = [[0 for _ in range(length)] for _ in range(length)]

    for y in range(length):
        for x in range(length - 1, -1, -1):
            newKey[y][length - x - 1] = key[x][y]

    return newKey


# 실제 lock 부분만 확인
def check(expendedLock):
    for x in range(M - 1, M + N - 1):
        for y in range(M - 1, M + N - 1):
            if expendedLock[x][y] == 0 or expendedLock[x][y] == 2:
                return False
    return True

# key를 위치에 따라 더해줌
def puzzle(key, expendedLock):
    newOne = deepcopy(expendedLock)
    # print(newOne)
    for startX in range(0, M + N - 1):
        for startY in range(0, M + N - 1):
            for x in range(M):
                for y in range(M):
                    newOne[startX + x][startY + y] += key[x][y]
            # print(newOne)
            # return
            if check(newOne):
                return True
            else:
                newOne = deepcopy(expendedLock)
    return False
