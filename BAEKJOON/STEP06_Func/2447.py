def makeStar(n):
    if n == 3:
        star = ['***', '* *', '***']
        return star
    else:
        temp = makeStar(n / 3)[:]
        for i in range(len(temp)):
            temp[i] = temp[i] * 3
        temp2 = makeStar(n / 3)[:]
        for i in range(len(temp2)):
            temp2[i] += (temp2[i].replace('*', ' ') + temp2[i])
        return temp + temp2 + temp


ans = makeStar(int(input()))
for i in range(len(ans)):
    print(ans[i])
