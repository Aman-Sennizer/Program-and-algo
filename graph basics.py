n,m=map(int,input().split())

g=[[] for i in range(n)]

for _ in range(m):
    v1,v2=map(int,input().split())
    v1-=1;v2-=1
    g[v1].append(v2)


def dfs(i):
    maxi=0
    for nv in g[i]:
        maxi=max(maxi,dfs(nv)+1)
    return maxi
maxo=0
for i in range(n):
    maxo=max(maxo,dfs(i))
print(maxo)
