class_num=int(input())
result=[]
while class_num!=0:
    score=list(map(int,input().split()))
    average=(sum(score)-score[0])/score[0]
    count=0
    for i in score:
        if i==score[0]: continue
        elif i>average: count+=1
    result.append(count/score[0]*100)
    class_num-=1
for i in result:
    print("%0.3f%%" %i)