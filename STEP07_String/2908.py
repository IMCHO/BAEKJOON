twoNumber = [num for num in input().split()]
for (index, num) in enumerate(twoNumber):
    twoNumber[index] = (num[2] + num[1] + num[0])
print(int(twoNumber[0] if int(twoNumber[0]) > int(twoNumber[1]) else int(twoNumber[1])))
