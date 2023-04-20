a=[-2,-3,4,-1,-2,1,5,-3]
cur=a[0]
final=a[0]
for i in range(1,len(a)):
    cur=max(a[i],cur+a[i])
    final=max(cur,final)
print(final)