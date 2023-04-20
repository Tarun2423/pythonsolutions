arr=[]
def check(i,j,a,c):
    if i<0 or j<0 or i>2 or j>2:
        return 0

    if j<2 and a[i][j]+1==a[i][j+1]:
        check(i,j+1,a,c+1)
    if j>0 and a[i][j]+1==a[i][j-1]:
        check(i,j-1,a,c+1)
    if i<2 and a[i][j]+1==a[i+1][j]:
        check(i+1,j,a,c+1)
    if i>0 and a[i][j]+1==a[i-1][j]:
        check(i-1,j,a,c+1)
    else:
        if c==1:
            pass
        else:
            arr.append(c)
        return 0
a=[[1,6,7],
[2,5,8],
[3,4,9]]
c=1
for i in range(3):
    for j in range(3):
        check(i,j,a,c)
print(max(arr))
