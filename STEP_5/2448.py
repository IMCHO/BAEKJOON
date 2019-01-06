def printStar(n1, n2):
    temp = (5 * pow(2, n1) + pow(2, n1) - 1) // 2
    print(' ' * temp + '*' + ' ' * (temp * 2 + 1) + '*' * n2)
    print(' ' * (temp - 1) + '* *' + ' ' * ((temp - 1) * 2 + 1) + '* *' * n2)
    print(' ' * (temp - 2) + '*****' + ' ' * ((temp - 2) * 2 + 1) + '*****' * n2)
    while (n1 > 0):
        n1 -= 1
        n2 += 1
        printStar(n1, n2)


num = int(input())
a, b = 3, 2
c = (num // a // b)
printStar(c, 0)
