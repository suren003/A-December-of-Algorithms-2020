a=int(input("Room: "))
temp=a*a
check=1
while check:
    if temp//(10**check)!=0:
        check+=1
    else:
        break    
if a%3!=0:
    print("Status: Not Safe")
else:
    b=temp//(10**(check//2))
    c=temp%(10**(check//2))
    if check%2==0:
        if b+c == a:
            print("Status: Safe")
        else:
            print("Status: Not Safe")
    else:
        if b+c == a:
            print("Status: Safe")
        else:
            b=temp//(10**((check//2)+1))
            c=temp%(10**((check//2)+1))
            if b+c == a:
                print("Status: Safe")
            else:
                print("Status: Not Safe")

        
        
