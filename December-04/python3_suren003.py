def isleap(x):
    if x%400 == 0:
        return True
    elif x%100 != 0 and x%4 == 0:
        return True
    else:
        return False
n=int(input("Number of Ice Creams : "))
dates=input("Manufacture Dates : ")
bbday=input("Best Befor days : ")
givendate=input("Given date : ")
bbday=bbday.split()
mo=map(int,bbday)
bbday=list(mo)
i=0
c=""
count=0
date=[]
givendat=[]
while i<len(dates):
    if dates[i].isnumeric():
        c+=(dates[i])
        if not(dates[i+1].isnumeric()):
            date.append(int(c))
            c=""
    i+=1
i=0
c=""
while i<len(givendate):
    if givendate[i].isnumeric():
        c+=(givendate[i])
        if not(givendate[i+1].isnumeric()):
            givendat.append(int(c))
            c=""
    i+=1
i=0
while i<len(date)//3:
    date[i*3]+=bbday[i]
    while date[i*3]>30:
        date[i*3]-=30
        date[i*3+1]+=1
        if date[i*3+1]>12:
            date[i*3+1]-=12
            date[i*3+2]+=1
    if givendat[2]<date[i*3+2]:
        count+=1
    elif givendat[2]==date[i*3+2] and givendat[1]<date[i*3+1]:
        count+=1
    elif givendat[2]==date[i*3+2] and givendat[1]==date[i*3+1] and givendat[0]<=date[i*3]:
        count+=1
    else:
        pass
    i+=1
print("\nNo of ice creams spoiled:",n-count)
