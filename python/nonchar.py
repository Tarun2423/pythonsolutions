s="amcam"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
c=0
for i,j in d.items():
    if j==1:
        c+=1
print(c)