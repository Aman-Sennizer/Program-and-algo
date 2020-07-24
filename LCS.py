def lenLcs(s1,s2,i,j,dp):
    if i>=len(s1) or j>=len(s2):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s1[i]==s2[j]:
        dp[i][j]= 1+lenLcs(s1,s2,i+1,j+1,dp)
        return dp[i][j]
    else:
        dp[i][j]=(max(lenLcs(s1,s2,i,j+1,dp),lenLcs(s1,s2,i+1,j,dp)))
    return dp[i][j]

#def printLcs(s1,s2,
                
s1="axyb"
s2="abyxb"
dp=[[-1 for _ in range(len(s2)+1)] for _ in range(len(s2)+1)]
print(lenLcs(s1,s2,0,0,dp))
print(dp)
