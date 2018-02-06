standard=list(map(int,input().split()))
num=list(map(int,input().split()))
def Check(n1):
    if n1<standard[1]: return n1
result=list(filter(Check,num))
for i in result:
    print(i,end=' ')
