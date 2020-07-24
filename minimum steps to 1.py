def minsteps(n):
    if n==1:
        return 0
    a=minsteps(n-1)
    if n%2==0:
        b=minsteps(n//2)
    else:
        b=1000000007

    if n%3==0:
        c=minsteps(n//3)
    else:
        c=1000000007
    return min(a,min(b,c))+1

print(minsteps(10))
