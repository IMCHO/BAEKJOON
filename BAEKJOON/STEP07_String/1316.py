case = int(input())
notResult = 0
for _ in range(case):
    word = input()
    checked = [""]
    for c in word:
        temp = checked.pop()
        if c == temp:
            checked.append(temp)
            continue
        checked.append(temp)
        if checked.count(c) == 1:
            notResult += 1
            break
        else:
            checked.append(c)
print(case - notResult)
