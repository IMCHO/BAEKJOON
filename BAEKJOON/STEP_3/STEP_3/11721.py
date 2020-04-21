str=input()
num=list(divmod(len(str),10))
strlist=[]
start=0
end=10
while num[0]!=-1:
    if end>len(str): end=start+num[1]
    strlist.append(str[start:end])
    start+=10
    end+=10
    num[0]-=1
    if num[0]==0 and num[1]==0: break
for i in strlist:
    print(i)
