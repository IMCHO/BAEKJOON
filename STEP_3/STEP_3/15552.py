import sys
count=int(input())
while count!=0:
    string=sys.stdin.readline()
    string=string.rstrip()
    index=string.find(' ')
    print(int(string[0:index])+int(string[index+1:]))
    count-=1