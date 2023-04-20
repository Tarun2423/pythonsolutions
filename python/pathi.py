a=[[1,1,1,1],
[0,1,0,0],
[1,0,1,1]]
def dfs(i,j):
    if i<0 or j<0 or i>=len(a) or j>=len(a[0]) or a[i][j]!=1:
        return
    a[i][j]=-1
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)
dfs(0,0)
if a[len(a)-1][len(a[0])-1]==-1:
    print("yes")
else:
    print("no")