count=int(input())
star='*'
empty=' '
num=1
while count!=0:
    a=star*count
    b=empty*(num-1)
    print("%s%s" %(b,a))
    num+=1
    count-=1