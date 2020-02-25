N = int(input())
init = 665
while N != 0:
    init += 1
    strNum = str(init)
    if strNum.count('666') >= 1:
        N -= 1

print(init)