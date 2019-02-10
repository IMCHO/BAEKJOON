results=[]
for _ in range(int(input())):
    temp=input().split(" ")
    results.append(list(map(lambda s:s*int(temp[0]),temp[1])))
for result in results:
    print("".join(result))