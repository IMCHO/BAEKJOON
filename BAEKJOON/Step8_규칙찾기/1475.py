dict = {}
for num in input():
    if num == '9':
        dict['6'] = dict.get('6', 0) + 1
    else:
        dict[num] = dict.get(num, 0) + 1
dict['6'] = (dict.get('6', 0) + 1) // 2
print(max(dict.values(), default=0))
