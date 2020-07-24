n=int(input())
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0]=1.0
coins=list(map(float,input().split()))
for i in range(1,len(coins)+1):
    for j in range(len(coins)+1):
        if j==0:
            dp[i][0]=(1.0-coins[i-1])*dp[i-1][0]


        else:
            dp[i][j]=(coins[i-1]*dp[i-1][j-1])+(dp[i-1][j]*(1.0-coins[i-1]))
res=0
for  i in range(n//2+1,n+1):
    res=res+dp[n][i]
print(res)
