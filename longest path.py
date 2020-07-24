n,m=map(int,input().split())
graph=[[] for _ in range(n)]
print(graph)
for i in range(m):
       p1,p2=map(int,input().split())
       graph[p1-1].append(p2-1)
print(graph)
