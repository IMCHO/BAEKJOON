def solution(m, n, puddles):
    routes = [[0, 0]]
    copiedPuddles = list(map(lambda x: [x[0] - 1, x[1] - 1], puddles))

    while True:
        routeForExtension = []
        for route in routes:
            down = [route[0], route[1] + 1]
            right = [route[0] + 1, route[1]]

            if down[1] < n and down not in copiedPuddles:
                routeForExtension.append(down)
            if right[0] < m and right not in copiedPuddles:
                routeForExtension.append(right)

        if [m - 1, n - 1] in routeForExtension:
            break
        else:
            routes = routeForExtension

    return routeForExtension.count([m - 1, n - 1]) % 1000000007
