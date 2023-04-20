s="hello mu dear friendsaa"
ac=ec=ic=oc=uc=0
for i in s:
    if i=='a' or i=='A':
        ac+=1
    elif i=='e' or i=='E':
        ec+=1
    elif i=='i' or i=='I':
        ic+=1
    elif i=='o' or i=='O':
        oc+=1
    elif i=='u' or i=='U':
        uc+=1
a=[]
a.append(ac)
a.append(ec)
a.append(ic)
a.append(oc)
a.append(uc)
c=a[:]
b=[0,1,2,3,4]
si=0
for i in range(len(a)):
    m=a[i]
    for j in range(i+1,len(a)):
        if a[j]<m:
            a[i],a[j]=a[j],a[i]
            m=a[j]
            b[i],b[j]=b[j],b[i]
d=['A','E','I','O','U']
for i in reversed(b):
    if c[i]!=0:
        print(d[i],c[i])
    