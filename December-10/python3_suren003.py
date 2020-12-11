def crlog(x):
   if len(x)>3: 
    lis=[]
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                for l in range(1,4):
                    if i+j+k+l==len(x):
                        if (x[0]!='0' or len(x[0:i])==1) and (x[i]!='0' or len(x[i:i+j])==1) and (x[i+j]!='0' or len(x[i+j:i+j+k])==1) and (x[i+j+k]!='0' or len(x[i+j+k:])==1):
                            if int(x[0:i])<=255 and int(x[i:i+j])<=255 and int(x[i+j:i+j+k])<=255 and int(x[i+j+k:])<=255:
                                temp=x[0:i]+"."+x[i:i+j]+"."+x[i+j:i+j+k]+"."+x[i+j+k:]
                                lis.append(temp)
    return lis
x=str(input("Input: corrupted_log = "))
x=x.replace('"', "")
a=crlog(x)
print("Output: ",end="")
print(a)