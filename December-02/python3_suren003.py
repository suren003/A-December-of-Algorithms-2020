a=[['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
b=int(input("Input: "))
c=b%10-2
b=(b//10)-2
print("Output: [",end="")
if b>=0 and c>=0:
    for i in a[b]:
        for j in a[c]:
            temp='"'+i+j+'"'
            if not(i==a[b][-1] and j==a[c][-1]):
                temp+=','
            print(temp,end="")
print("]")
            
            


