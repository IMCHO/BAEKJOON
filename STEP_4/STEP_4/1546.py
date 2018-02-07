count=int(input())
exam=list(map(int,input().split()))
print("%0.2f" %(sum(exam)/max(exam)*100/count))
