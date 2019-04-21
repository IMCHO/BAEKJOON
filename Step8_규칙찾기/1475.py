dict = {}
for num in input():
    if num == '9':
        dict['6'] = dict.get('6', 0) + 1
    else:
        dict[num] = dict.get(num, 0) + 1
sixOrNine = dict.get('6', 0)
dict['6'] = 0
maxCnt = max(dict.values())
if sixOrNine / 2 <= maxCnt:
    print(maxCnt)
else:
    if sixOrNine % 2 == 0:
        print(sixOrNine // 2)
    else:
        print(sixOrNine // 2 + 1)
