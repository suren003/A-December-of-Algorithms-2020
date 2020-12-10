def sum1(lis,x,y,a):
    if lis[x][y]!=0:
        sume=sum(lis[x])
        for i in range(x+1,int(a[0])):
            sume+=lis[i][y]
        return sume
    else:
        return 999999

def makezeros(lis,x,y,a):
    for i in range(x,int(a[0])):
        lis[i][y]=0
    return lis

a=input("Input : ")
a=list(a.split(" "))
b=[]
count=0
for i in range(0,int(a[0])):
    temp=input()
    temp1=[]
    for j in temp:
        if j=='U':
            temp1.append(1)
        else:
            temp1.append(0)
    b.append(temp1)

for i in range(0,int(a[0])):
    calc=[]
    for j in range(0,int(a[1])):
        calc.append(sum1(b,i,j,a))
    if min(calc)!=999999:
        count+=1
        b=makezeros(b,i,calc.index(min(calc)),a)

print("\nOutput :",count)







