n=int(input())
l=list(map(int,input().split()))
dp=[0]*len(l)
for i in range(1,len(l)):
    m=1000000007
    for j in range(1,3):
        if i-j>=0:
            m=min(m,(abs(l[i]-l[i-j])+dp[i-j]))
            dp[i]=m
print(dp[-1])
