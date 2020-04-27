'''
    Make a dictionary for map by '+5, -5, +1,-1'.
    Get a direction depending on '+5, -5, +1,-1'.
    Count how many changing direction until meeting hole.
    If it is under 10, get a minimum value.
    If these are all over 10, print -1.
    See where blue is moving to while red is moving.
'''
from collections import deque

row, col = map(int, input().split())
map = []
for _ in range(row):
    map.append(list(input()))

xR, yR, xB, yB = 0, 0, 0, 0
xD, yD = 0, 0
for index, line in enumerate(map):
    if 'R' in line:
        xR, yR = index, line.index('R')
    if 'B' in line:
        xB, yB = index, line.index('B')
    if 'O' in line:
        xD, yD = index, line.index('O')
# print(xR,yR,xB,yB,xD,yD)