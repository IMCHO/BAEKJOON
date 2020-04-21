a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
score=(a,b,c,d,e)
sum=0
for s in score:
    if s>=40:
        sum+=s
    else:
        sum+=40
print(sum//5)