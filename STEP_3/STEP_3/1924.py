
month,day=input().split()
month=int(month)
day=int(day)
sum=0
month-=1
week={1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',0:'SUN'}
cal={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
while month!=0:
    sum+=cal[month]
    month-=1
sum+=day
print("%s" %week[sum%7])
