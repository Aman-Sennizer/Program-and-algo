def mincoin(n,l):
    if n==0:
        return 0

    ans=1000000009
    for i in range(len(l)):
        if n-l[i]>=0:
            sub=mincoin(n-l[i],l)
            ans=min(ans,sub+1)
    return ans

print(mincoin(10,[1,5,3]))
