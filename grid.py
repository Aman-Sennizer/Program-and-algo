h,w=map(int,input().split())
l=[[input() for _ in range(w)] for _ in range(h)]
dp=[[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if l[i][j]!='.':
            if l[i+1][j]!='#':
                dp[i+1][j]=1
            else:
                dp[i+1][j]=0
            if l[i][j+1]!='#':
                dp[i][j+1]=1
            else:
                dp[i][j+1]=0

        if l[i][j]=='#':
            dp[i][j]=0
            if l[i+1][j]!='#':
                dp[i+1][j]=1
            else:
                dp[i+1][j]=0
            if l[i][j+1]!='#':
                dp[i][j+1]=1
            else:
                dp[i][j+1]=0
        
