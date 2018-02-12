num=input()
temp=num
temp2=0
cycle=0
while True:
    for i in temp:
        temp2+=int(i)
    temp=temp[len(temp)-1]+str(temp2)[len(str(temp2))-1]
    if temp==num:
        cycle+=1;break
    else: cycle+=1
print(cycle)