n,k=map(int,input().split())
v=list(map(int,input().split()))
mod=10**9
dp=[[0 for _ in range(k+3)] for _ in range(n+3)]
for j in range(0,k+1):
    if j>=v[1]:
        dp[1][j]=0
    else:
        dp[1][j]=1

for i in range(2,n):
    for j in range(0,k+1):
        if j==0:
            dp[i][j]=dp[i-1][j]
        else:
            if (j-v[i-1]-1)>=0:
                dp[i][j]=(mod+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-v[i-1]-1])%mod
            else:
                dp[i][j]=(mod+dp[i][j-1])%mod
print(dp)
