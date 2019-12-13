x, y, w, h = map(int, input().split())
hori = (w - x) if x >= (w / 2) else x
verti = (h - y) if y >= (h / 2) else y
print(min(hori, verti))
