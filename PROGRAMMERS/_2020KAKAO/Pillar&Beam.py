def solution(n, build_frame):
    frames = []

    for frame in build_frame:
        x, y, a, b = frame
        if a == 0 and b == 0:
            frames.remove([x, y, 0])
            if not check(frames): frames.append([x, y, 0])
        elif a == 0 and b == 1:
            frames.append([x, y, 0])
            if not check(frames[::-1]): frames.remove([x, y, 0])
        elif a == 1 and b == 0:
            frames.remove([x, y, 1])
            if not check(frames): frames.append([x, y, 1])
        else:
            frames.append([x, y, 1])
            if not check(frames[::-1]): frames.remove([x, y, 1])

    answer = sorted(frames, key=lambda x: (x[0], x[1], x[2]))
    return answer


def check(frames):
    for frame in frames:
        x, y, a = frame

        if a == 0:
            if y == 0 or [x - 1, y, 1] in frames or [x, y, 1] in frames or [x, y - 1, 0] in frames:
                continue
            else:
                return False
        else:
            if [x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames or (
                    [x - 1, y, 1] in frames and [x + 1, y, 1] in frames):
                continue
            else:
                return False
    return True
