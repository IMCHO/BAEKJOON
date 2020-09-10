def solution(n, build_frame):
    answer = [[]]
    points = []

    for frame in build_frame:
        x, y, a, b = frame
        # set pillar
        if a == 0 and b == 1:
            if y == 0 \
                    or [x, y - 1, 0] in points \
                    or ([x - 1, y, 1] in points and [x, y, 1] not in points) \
                    or ([x - 1, y, 1] not in points and [x, y, 1] in points):
                points.append([x, y, 0])
        # set beam
        elif a == 1 and b == 1:
            if [x, y, 0] in points \
                    or [x + 1, y, 0] in points \
                    or ([x - 1, y, 1] in points and [x + 1, y, 1] in points):
                points.append([x, y, 1])
        # remove pillar
        elif a == 0 and b == 0:
            if [x, y + 1, 1] in points:
                if ([x - 1, y + 1, 1] in points and [x + 1, y + 1, 1] in points) or [x + 1, y, 0] in points:
                    points.remove([x, y, 0])
            elif [x - 1, y + 1, 1] in points:
                if ([x - 2, y + 1, 1] in points and [x, y + 1, 1] in points) or [x - 1, y, 0] in points:
                    points.remove([x, y, 0])
            elif [x, y + 1, 0] in points:
                continue
            else:
                points.remove([x, y, 0])

        elif a == 1 and b == 0:
            if ([x, y, 0] in points and ([x - 1, y, 1] not in points or [x, y - 1, 0] not in points)) \
                    or ([x + 1, y, 0] in points and ([x + 1, y, 1] not in points or [x + 1, y - 1, 0] not in points)) \
                    or ([x + 1, y, 1] in points and [x + 1, y - 1, 0] not in points and [x + 2, y - 1, 0] not in points) \
                    or ([x - 1, y, 1] in points and [x, y - 1, 0] not in points and [x - 1, y - 1, 0] not in points):
                continue
            points.remove([x, y, 1])

    answer = sorted(points, key=lambda x: (x[0], x[1], x[2]))
    return answer
