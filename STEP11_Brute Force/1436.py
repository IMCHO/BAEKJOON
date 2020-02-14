N = int(input())
init = 665
while N != 0:
    strNum = str(init)
    if strNum.count('6') == 3:
        start = strNum.index('6')
        if strNum[start:start + 3] == '666':
            N -= 1
    init += 1

print(init - 1)
