a=input("Counter A: ")
a=" ".join(a.split())
a=list(a.split(" "))
b=input("Counter B: ")
b=" ".join(b.split())
b=list(b.split(" "))
c=[]
i=0
j=0
while j<len(b) or i<len(a):
    if j<len(b)-1:
        c.append(b[j])
        c.append(b[j+1])
        j+=2
    elif j<len(b):
        c.append(b[j])
        j+=1
    if i<len(a):
        c.append(a[i])
        i+=1
print("\nTemperature Screening: ",end="")
for i in c:
    print(i,end="  ")
print("\n")