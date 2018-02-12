num=input()
temp=num
cycle=0
while True:
    if int(temp)<10:
        temp=temp+temp
    else:
        if int(temp[0])+int(temp[1])<10:
            temp=temp[1]+str(int(temp[0])+int(temp[1]))[0]
            if(temp==num): break
            else: cycle+=1
        else: 
            temp=temp[1]+str(int(temp[0])+int(temp[1]))[1]
            if(temp==num): break
            else: cycle+=1
print(cycle+1)