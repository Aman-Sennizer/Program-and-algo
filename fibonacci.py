def fib(n,dp):
    if n==0 or n==1:
        return 1
    if dp[n]!=0:
        return dp[n]
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]

n=int(input())
dp=[0 for _ in range(n+1)]
print(fib(n,dp))
