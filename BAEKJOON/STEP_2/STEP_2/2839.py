
sugar=int(input())
five=sugar//5
three=0
list=[]
while five!=-1:
	remain=sugar-five*5
	if remain==0: list.append(five)
	else:
		if remain%3==0:
			three=remain//3
			list.append(five+three)
	five-=1
list.sort()
if list:
	print(list.pop(0))
else:
	print(-1)