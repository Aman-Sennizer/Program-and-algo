lw=[]
lp=[]
n,w=input().split()
dp=[[0 for _ in range(n+1)] for _ in range(w+1)]   
n=int(n)
w=int(w)
for _ in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    lw.append(a)
    lp.append(b)

for i in range(n):
    for j in range(w):
        
