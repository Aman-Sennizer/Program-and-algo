n=int(input())
l=[]
dp=[0]*(n+1)
for _ in range(n):
    l.append(list(map(int,input().split())))
for i in range(1,len(l)):
    m=0
    for j in range(2):
        if j==0:
            a=0
        else:
            a=l[i][j]+l[i-1][0]
        if j==1:
            b=0
        else:
            b=l[i][j]+l[i-1][1]
        if j==2:
            c=0
        else:
            c=l[i][j]+l[i-1][2]
        m=max(a,b,c,m)
        dp[i]=m
print(dp)
        
        
        
    
    
