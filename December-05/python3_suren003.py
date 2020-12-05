class cell: 
    def __init__(self, x = 0, y = 0, dist = 0): 
        self.x = x 
        self.y = y 
        self.dist = dist 
          
def ispresent(x, y, N): 
    if (x >= 1 and x <= N and y >= 1 and y <= N):  
        return True
    return False
      
def minstep(knightpos, targetpos, N): 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
    queue = [] 
    queue.append(cell(knightpos[0], knightpos[1], 0)) 
    visited = [[False for i in range(N + 1)]for j in range(N + 1)] 
    visited[knightpos[0]][knightpos[1]] = True
    while(len(queue) > 0): 
        t = queue[0] 
        queue.pop(0) 
        if(t.x == targetpos[0] and 
           t.y == targetpos[1]): 
            return t.dist 
        for i in range(8): 
            x = t.x + dx[i] 
            y = t.y + dy[i]   
            if(ispresent(x, y, N) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1)) 
n=input("Dimension of Board : ")
n=n.split()
n=map(int,n)
n=list(n)
n=n[0]
b=input("Position of Knight : ")
b=b.split()
b=map(int,b)
b=list(b)
t=input("Target Position :  ")
t=t.split()
t=map(int,t)
t=list(t)
print("\nMinimum Steps :",minstep(b,t,n))
