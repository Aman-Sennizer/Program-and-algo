
memory={}
def pascalSpot(row,col):
    index=(row,col)
    if index in memory:
        return memory[index]
    if col==1 or row==col:
        return 1
    upleft=pascalSpot(row-1,col-1)
    upright=pascalSpot(row-1,col)
    memory[index]=upleft+upright
    return upleft+upright

for r in range(1,25):
    print(' '*(25-r),end=" ")
    for c in range(1,r+1):
        print(pascalSpot(r,c),end=' ')
    print(' ')
    
