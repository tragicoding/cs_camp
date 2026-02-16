import datetime as d
now=d.datetime.now()
month=now.month
day=now.day
if len(str(now.month))==2:
    month=now.month
elif len(str(now.month))==1:
    month="0"+str(now.month)
if len(str(now.day))==2:
    day=now.day
elif len(str(now.day))==1:
    day="0"+str(now.day)


print("{}-{}-{}".format(now.year,month,day))