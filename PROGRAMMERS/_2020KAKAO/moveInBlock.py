from collections import deque
from copy import deepcopy


def solution(board):
    global size
    global trace
    size = len(board)
    answer = 0
    BFS = deque([[[[0, 0], [0, 1]], 0]])
    trace = [[[0, 0], [0, 1]]]
    offsets = [[[0, 1], [0, 1]],
               [[0, -1], [0, -1]],
               [[1, 0], [1, 0]],
               [[-1, 0], [-1, 0]]]
    while BFS:
        nowPos, cnt = BFS.popleft()

        for newOne in moveWork(board, nowPos, cnt, offsets):
            if isEndPoint(newOne[0]): return newOne[1]
            BFS.append(newOne)

        for newOne in rotationWork(board, nowPos, cnt):
            if isEndPoint(newOne[0]): return newOne[1]
            BFS.append(newOne)

    return answer


def isEndPoint(nowPos):
    p1, p2 = nowPos
    x1, y1 = p1
    x2, y2 = p2

    if (x1 == size - 1 and y1 == size - 1) \
            or (x2 == size - 1 and y2 == size - 1):
        return True
    else:
        return False


def checkRange(value):
    if 0 <= value < size:
        return True
    else:
        return False


def canMove(board, nowPos):
    p1, p2 = nowPos
    x1, y1 = p1
    x2, y2 = p2
    for p in [x1, x2, y1, y2]:
        if not checkRange(p): return False
    if board[x1][y1] == 1 or board[x2][y2] == 1:
        return False
    else:
        return True


def moveWork(board, nowPos, cnt, offsets):
    p1, p2 = nowPos
    x1, y1 = p1
    x2, y2 = p2
    result = []

    for offset in offsets:
        offsetP1, offsetP2 = offset
        xOffsetP1, yOffsetP1 = offsetP1
        xOffsetP2, yOffsetP2 = offsetP2

        copiedCnt = cnt
        newPos = [[x1 + xOffsetP1, y1 + yOffsetP1], [x2 + xOffsetP2, y2 + yOffsetP2]]
        if canMove(board, newPos) and newPos not in trace:
            trace.append(newPos)
            copiedCnt += 1
            result.append([newPos, copiedCnt])
    return result


def rotationWork(board, nowPos, cnt):
    p1, p2 = nowPos
    x1, y1 = p1
    x2, y2 = p2
    result = []

    if x1 == x2:
        downPos1 = [[x1, y1], [x1 + 1, y1]]
        downPos2 = [[x2, y2], [x2 + 1, y2]]
        if canMove(board, downPos1) and canMove(board, downPos2):
            copiedCnt = cnt
            if downPos1 not in trace:
                trace.append(downPos1)
                copiedCnt += 1
                result.append([downPos1, copiedCnt])

            copiedCnt = cnt
            if downPos2 not in trace:
                trace.append(downPos2)
                copiedCnt += 1
                result.append([downPos2, copiedCnt])

        upPos1 = [[x1 - 1, y1], [x1, y1]]
        upPos2 = [[x2 - 1, y2], [x2, y2]]
        if canMove(board, upPos1) and canMove(board, upPos2):
            copiedCnt = cnt
            if upPos1 not in trace:
                trace.append(upPos1)
                copiedCnt += 1
                result.append([upPos1, copiedCnt])

            copiedCnt = cnt
            if upPos2 not in trace:
                trace.append(upPos2)
                copiedCnt += 1
                result.append([upPos2, copiedCnt])

    elif y1 == y2:
        leftPos1 = [[x1, y1 - 1], [x1, y1]]
        leftPos2 = [[x2, y2 - 1], [x2, y2]]
        if canMove(board, leftPos1) and canMove(board, leftPos2):
            copiedCnt = cnt
            if leftPos1 not in trace:
                trace.append(leftPos1)
                copiedCnt += 1
                result.append([leftPos1, copiedCnt])

            copiedCnt = cnt
            if leftPos2 not in trace:
                trace.append(leftPos2)
                copiedCnt += 1
                result.append([leftPos2, copiedCnt])

        rightPos1 = [[x1, y1], [x1, y1 + 1]]
        rightPos2 = [[x2, y2], [x2, y2 + 1]]
        if canMove(board, rightPos1) and canMove(board, rightPos2):
            copiedCnt = cnt
            if rightPos1 not in trace:
                trace.append(rightPos1)
                copiedCnt += 1
                result.append([rightPos1, copiedCnt])

            copiedCnt = cnt
            if rightPos2 not in trace:
                trace.append(rightPos2)
                copiedCnt += 1
                result.append([rightPos2, copiedCnt])

    return result
