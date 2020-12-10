from collections import deque

def findCompletionOrderOfTasks(a):
    que1=deque()
    que2=deque()
    que1.append('A')
    while(len(que1)!=0):
        temp=que1.popleft()
        if ord(temp)-65<len(a):
            for i in a[ord(temp)-65]:
                que1.append(i)
            que2.append(temp)
        else:
            que2.append(temp)
    return que2
a=input()
a=list(a)
i=0
at=[]
while i<len(a):
    if a[i]=='[':
        b=[]
        while a[i]!=']':
            if a[i]<='Z' and a[i]>='A':
                b.append(a[i])
            i+=1
        at.append(b)
    i+=1
print(' '.join(list(findCompletionOrderOfTasks(at))))
