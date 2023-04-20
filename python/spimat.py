# a=[[1,2,3,4,5],
# [6,7,8,9,10],
# [10,11,12,13,14],
# [15,16,17,18,19],
# [20,21,22,23,24]]
a=[[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]]
al=len(a)
for i in range(al//2):
    for j in range(i,len(a[0])-i-1):
        print(a[i][j])
    for k in range(i,len(a[0])-i-1):
        print(a[k][al-1-i])
    for l in range((al-1)-i,i,-1):          
        print(a[al-1-i][l])             
    for m in range((al-1)-i,i,-1):
        print(a[m][i])
    