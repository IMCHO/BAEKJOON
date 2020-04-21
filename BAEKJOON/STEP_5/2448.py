import math

star=['  *   ',' * *  ','***** ']


def printStar(n1):
        for i in range(len(star)):
            star.append(star[i]+star[i])
            star[i]=('   '*n1+star[i]+'   '*n1)


num = int(input())
k=int(math.log(num//3,2))
for i in range(k):
    printStar(pow(2,i))

for i in range(len(star)):
    print(star[i])

