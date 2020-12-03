inpstr=input("Input: ")
i=0
a=[]
b=[]
c=[]
d=[]
while(i<len(inpstr)):
    if inpstr[i].isnumeric():
        hr=(inpstr[i:i+2])
        mi=(inpstr[i+2:i+4])
        i+=4
        temp=int(hr)*60+int(mi)
        temp1=hr+mi
        a.append(temp)
        b.append(temp1)
    else:
        i+=1
i=1
while(i<(len(a)-1)):
    if a[i+1]-a[i]>=60:
        c.append(b[i])
        c.append(b[i+1])
        d.append(c)
        c=[]
        i+=2
    else:
        i+=2
print("Output: ",end="")
for i in d:
    print('["',end="")
    print(i[0],end="")
    print('","',end="")
    print(i[1],end="")
    print('"]',end="")
    if d.index(i)<(len(d)-1):
        print(",",end="")


        



