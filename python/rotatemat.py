# a=[[1,2,3,4],
# [5,6,7,8],
# [9,10,11,12],
# [13,14,15,16],
# [17,18,19,20]]
a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
m=len(a)//2
r=len(a)
c=len(a[0])
for i in range(m):
    prev=a[i][i]
    for j in range(i+1,c):
        cur=a[i][j]
        a[i][j]=prev
        prev=cur
    for j in range(i+1,r):
        cur=a[j][c-1]
        a[j][c-1]=prev
        prev=cur
    for j in range(c-1,i,-1):
        cur=a[r-1][j-1]
        a[r-1][j-1]=prev
        prev=cur
    for j in range(r-1,i,-1):
        cur=a[j-1][i]
        a[j-1][i]=prev
        prev=cur
    r-=1
    c-=1
    print(a)
