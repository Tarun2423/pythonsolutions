a=list(map(int,input.split()))
n=a[0]
c=a[1]
b=a[2:]
d=[]
for i in b:
    if i>c or i<=0:
        print(-1)
    elif i not in d:
        d.append(i)
if len(d)!=c:
    print(-1)
    exit()
if(d==a[2:]):
    print(len(d))
    exit()
ct=[]
d=[]
e=[]
for i in range(1,c+1):
    d.append(i)
for i in range(n-c):
    co=2+i
    t=0
    while(t<=c):
        if(a[co] in d and a[co] not in e):
            e.append(a[co])
            t+=1
            co+=1
        elif(a[co] in d and a[co] in e):
            t+=1
            co+=1
        if(len(d)==len(e)):
            ct.append(t)
            e=[]
            t=0
            break
print(min(ct))

